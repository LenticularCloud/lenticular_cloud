{
  description = "Lenticular cloud interface";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    flake-compat = {
      url = "github:edolstra/flake-compat";
      flake = false;
    };
    nix-node-package = {
      url = "github:mkg20001/nix-node-package";
      flake = false;
    };
  };
  outputs = inputs@{ self, nixpkgs, nix-node-package, ...  }:
    let
      makeNode = nix-node-package.lib.nix-node-package.makeNode;
      node-env = makeNode { };
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
      python_default = pkgs.python310;
      nodejs = pkgs.nodejs;
      lenticular_cloud = {python}: with python.pkgs; let

        urlobject = buildPythonPackage rec {
          pname = "URLObject";
          version = "2.4.3";
          src = fetchPypi {
            inherit pname version;
            sha256 = "47b2e20e6ab9c8366b2f4a3566b6ff4053025dad311c4bb71279bbcfa2430caa";
          };
          doCheck = true;
          propagatedBuildInputs = [
          ];
        };
        flask-dance = with python.pkgs; buildPythonPackage rec {
          pname = "Flask-Dance";
          version = "6.0.0";
          src = fetchPypi {
            inherit pname version;
            sha256 = "15bb3c412eb789a2d904bfd0fd44aac2d94f82703a51d14123fd336136d55db0";
          };
          doCheck = false;
          propagatedBuildInputs = [
            requests
            oauthlib
            requests_oauthlib
            flask
            urlobject
          ];
          checkInputs = [
            pytest
            nose
            pytest-mock
            responses
            freezegun
            coverage
      # testing sqlalchemy support
            sqlalchemy
            flask_sqlalchemy
      # testing integration with other extensions
            flask_login
            flask-caching
            betamax
      # we need the `signedtoken` extra for `oauthlib`
      #      oauthlib[signedtoken]
          ];

        };
        ory-hydra-client = buildPythonPackage rec {
          pname = "ory-hydra-client";
          version = "2.0.3";
          src = ./libs/ory-hydra-client; 
      #    doCheck = false;
          propagatedBuildInputs = [
            urllib3
            python-dateutil
            attrs
            httpx
          ];
        };
      in
      buildPythonApplication rec { # TODO change to buildPythonApplication
        pname = "lenticular_cloud";
        version = "0.2";
        src = ./.;
        propagatedBuildInputs = [
          flask
          flask-restful
          flask_sqlalchemy
          flask_wtf
          flask-babel
          flask_login
          requests
          requests_oauthlib
          ldap3
          #ldap3-orm
          pyotp
          cryptography
          blinker
          ory-hydra-client
          authlib # as oauth client lib
          fido2 # for webauthn
          flask_migrate # db migrations

          nodejs
          #node-env
          gunicorn

          flask-dance
        ];
        testBuildInputs = with python.pkgs; [
          pytest
          pytest-mypy
          flask_testing
          tox

          types-dateutil

          nose
          mypy

        ];
        passthru = {
          inherit python;
          pythonPath = python.pkgs.makePythonPath propagatedBuildInputs;
        };


        doCheck = false;
        checkInputs = [
          pytest
        ] ++ lenticular_settings.testBuildInputs;
      };
    in {
      formatter.x86_64-linux = nixpkgs.legacyPackages.x86_64-linux.nixpkgs-fmt;
      #packages.x86_64-linux.default = import ./shell.nix { inherit pkgs; };
      # TODO

      packages.x86_64-linux.default = lenticular_cloud {python=python_default;}; 
      nixosModules = {
        default = (import "${self}/module.nix" { inherit lenticular_cloud; });
      };
    };

}


#ldap3-orm = with python.pkgs; buildPythonPackage rec {
#  pname = "ldap3-orm";
#  version = "2.7.0";
#  src = fetchPypi {
#    inherit pname version;
#    sha256 = "8783886d4ce90d66da61ce24619593a265b50f0de1fbebe86df95c6788661664";
#  };
#  doCheck = false;
#  propagatedBuildInputs = [
#    ldap3
#    six
#  ];#
#};

