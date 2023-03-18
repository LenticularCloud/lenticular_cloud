{ lenticular_cloud }: { config, pkgs, lib, modulesPath, ... }:
let
  python = pkgs.python310;
  gevent = python.pkgs.gevent;
  gunicorn = python.pkgs.gunicorn;
  psycopg2 = python.pkgs.psycopg2;
  lenticular-pkg = lenticular_cloud { inherit python;};
in
{
  options = with lib.options; {
    services.lenticular-cloud ={
      enable = mkEnableOption "lenticluar service enable";
    };
  };
  imports = [
  ];
  config = {
    environment.systemPackages = [ lenticular-pkg ];
    
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

      environment = let
        python_path = python.pkgs.makePythonPath [ lenticular-pkg gevent psycopg2];
      in {
        CONFIG_FILE = "/etc/lenticular_cloud/production.conf";
        PYTHONPATH =  "${lenticular-pkg.pythonPath}:${lenticular-pkg}/lib/python3.10/site-packages:${python_path}";
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
              ${lenticular-pkg}/bin/lenticular_cloud-cli db_upgrade
            '';
        ExecStart = ''${gunicorn}/bin/gunicorn lenticular_cloud.wsgi --name lenticular_cloud \
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
