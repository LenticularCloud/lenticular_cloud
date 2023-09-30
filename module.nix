{ config, pkgs, lib, ... }:
let
  cfg = config.services.lenticular-cloud;
  python = pkgs.python3;
in
{
  options = with lib.options; {
    services.lenticular-cloud ={
      enable = mkEnableOption "lenticluar service enable";
    };
  };
  config = {
    environment.systemPackages = [ pkgs.lenticular-cloud ];

    nixpkgs.overlays = [
      (import ./overlay.nix)
    ];
    
    users = {
      groups.lenticular = {
      };
      users.lenticular = {
        createHome = true;
        home = "/var/lib/lenticular";
        description = "web server";
        extraGroups = [
        ];
        group = "lenticular";
        isSystemUser = true;
      };
    };

    systemd.services.lenticular-cloud = {
      description = "lenticular account";
      after = [ "network.target" ];
      wantedBy = [ "multi-user.target" ];
      enable = cfg.enable;

      environment = let
        python_path = with python.pkgs; makePythonPath [ lenticular-cloud gevent psycopg2];
      in {
        CONFIG_FILE = "/etc/lenticular_cloud/production.conf";
        PYTHONPATH = "${python_path}";
        # PYTHONPATH =  "${lenticular-pkg.pythonPath}:${lenticular-pkg}/lib/python3.10/site-packages:${python_path}";
      };

      serviceConfig = {
        Type = "simple";
        WorkingDirectory = /var/lib/lenticular;
        #User="lenticular"; #done by gunicorn
        ExecStartPre = pkgs.writeScript "lenticular-cloud-server-init" ''
              #!/bin/sh
              #cat > /var/lib/lenticular/foobar.conf <<EOF
              #SECRET_KEY=""
              #EOF
              ${pkgs.lenticular-cloud}/bin/lenticular_cloud-cli db_upgrade
            '';
        ExecStart = ''${python.pkgs.gunicorn}/bin/gunicorn lenticular_cloud.wsgi --name lenticular_cloud \
              -u lenticular \
              -g lenticular \
              --workers 3 --log-level=info \
              --bind=unix:/run/lenticular.sock \
              -k gevent'';
        Restart = "on-failure";
      };
    };

  };
}
