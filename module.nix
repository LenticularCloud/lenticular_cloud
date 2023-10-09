{ config, pkgs, lib, ... }:
let
  cfg = config.services.lenticular-cloud;
  username = "lenticular_cloud";
  data_folder = "/var/lib/${username}";
  python = pkgs.python3;
in
{
  options = with lib.options; {
    services.lenticular-cloud ={
      enable = mkEnableOption "lenticluar service enable";
      domain = mkOption {
        type = lib.types.str;
        example = "account.example.com";
      };
      settings = mkOption {
        type = lib.types.attrs;
        default = rec {
          DOMAIN = cfg.domain;
          DATA_FOLDER = data_folder;
          PKI_PATH = "${DATA_FOLDER}/pki";
          # SQLALCHEMY_DATABASE_URI = "sqlite:////${DATA_FOLDER}/db.sqlite";
          SQLALCHEMY_DATABASE_URI = "postgresql://${username}@/${username}?host=/run/postgresql";
          HYDRA_ADMIN_URL=  "https://${config.services.ory-hydra.admin_domain}";
          HYDRA_PUBLIC_URL=  "https://${config.services.ory-hydra.public_domain}";
        };

      };
    };
  };
  config = {
    environment.systemPackages = [ pkgs.lenticular-cloud ];

    nixpkgs.overlays = [
      (import ./overlay.nix)
    ];
    
    users = {
      groups."${username}" = {
      };
      users."${username}" = {
        createHome = true;
        home = data_folder;
        description = "web server";
        extraGroups = [
          # "ory-hydra"
        ];
        group = username;
        isSystemUser = true;
      };
    };

    services.postgresql = {
      enable = true;
      ensureDatabases = [ username ];
      ensureUsers = [
        {
          name = username;
          ensurePermissions = {
            "DATABASE ${username}" = "All PRIVILEGES";
          };
        }
      ];
      identMap = ''
        # ArbitraryMapName systemUser DBUser
        superuser_map   ${username}   ${username}
      '';
    };

    services.nginx.enable = true;
    services.nginx.virtualHosts."${cfg.domain}" = {
      addSSL = true;
      enableACME = true;
      serverName = cfg.domain;
      locations."/" = {
        recommendedProxySettings = true;
        proxyPass = "http://unix:/run/${username}/web.sock";
      };
    };
    users.users.nginx.extraGroups = [ username ];

    systemd.services.lenticular-cloud = {
      description = "lenticular account";
      after = [ "network.target" ];
      wantedBy = [ "multi-user.target" ];
      requires = [ "ory-hydra.service" ];
      enable = cfg.enable;

      environment = let
        python_path = with python.pkgs; makePythonPath [ pkgs.lenticular-cloud gevent ];
      in {
        # CONFIG_FILE = "/etc/lenticular_cloud/production.conf";
        CONFIG_FILE = pkgs.writeText "lenticular-cloud.json" (builtins.toJSON cfg.settings);
        PYTHONPATH = "${python_path}";
        # PYTHONPATH =  "${lenticular-pkg.pythonPath}:${lenticular-pkg}/lib/python3.10/site-packages:${python_path}";
      };
      preStart = ''
        #cat > ${data_folder}/foobar.conf <<EOF
        #SECRET_KEY=""
        #EOF
        ${pkgs.lenticular-cloud}/bin/lenticular_cloud-cli db_upgrade
      '';

      serviceConfig = {
        Type = "simple";
        WorkingDirectory = data_folder;
        User = username;
        ExecStart = ''${python.pkgs.gunicorn}/bin/gunicorn lenticular_cloud.wsgi --name lenticular_cloud \
              --workers 3 --log-level=info \
              --bind=unix:/run/${username}/web.sock \
              -k gevent'';
        Restart = "on-failure";
        RuntimeDirectory = username;
      };
    };

  };
}
