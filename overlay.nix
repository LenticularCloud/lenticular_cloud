final: prev:
let
  pkgs = final.pkgs;
in {
  python3 = prev.python3.override {
    packageOverrides = final: prev: with final; {
      sqlalchemy = prev.sqlalchemy.overridePythonAttrs (old: rec {
        version = "2.0.19";
        src = pkgs.fetchFromGitHub {
          owner = "sqlalchemy";
          repo = "sqlalchemy";
          rev = "refs/tags/rel_${lib.replaceStrings [ "." ] [ "_" ] version}";
          hash = "sha256-97q04wQVtlV2b6VJHxvnQ9ep76T5umn1KI3hXh6a8kU=";
        };
        disabledTestPaths = old.disabledTestPaths ++ [ "test/typing" ];
      });
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
      flask-dance = buildPythonPackage rec {
        pname = "Flask-Dance";
        version = "7.0.0";
        format = "pyproject";
        src = fetchPypi {
          inherit pname version;
          sha256 = "a37dec5c3a21f13966178285d5c10691cd72203dcef8a01db802fef6287e716d";
        };
        doCheck = true;
        propagatedBuildInputs = [
          requests
          oauthlib
          requests_oauthlib
          flask
          urlobject
          flit-core
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

      ory-hydra-client = buildPythonPackage {
        pname = "ory-hydra-client";
        version = "2.0.3";
        src = ./libs/ory-hydra-client; 
        doCheck = false;
        propagatedBuildInputs = [
          urllib3
          python-dateutil
          attrs
          httpx
        ];
      };
      flask-sqlalchemy = prev.flask-sqlalchemy.overridePythonAttrs (old: rec {
        version = "3.1.1";
        # version = "3.0.3";
        src = fetchPypi {
          pname = "flask_sqlalchemy";
          inherit version;
          sha256 = "e4b68bb881802dda1a7d878b2fc84c06d1ee57fb40b874d3dc97dabfa36b8312";
        };
        propagatedBuildInputs = old.propagatedBuildInputs ++ [
          flit-core sqlalchemy
        ];
        nativeCheckInputs = old.nativeCheckInputs ++ [
          typing-extensions
        ];
      });
      flask = prev.flask.overridePythonAttrs (old: {
        propagatedBuildInputs = old.propagatedBuildInputs ++ flask.optional-dependencies.async;
      });
      lenticular-cloud = buildPythonPackage {
        pname = "lenticular_cloud";
        version = "0.3";
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
          authlib # as oauth client lib
          fido2 # for webauthn
          flask_migrate # db migrations
          flask-dance
          ory-hydra-client
          toml

          pkgs.nodejs
          #node-env
          gunicorn
          psycopg2
        ];
        testBuildInputs = [
          pytest
          pytest-mypy
          flask_testing
          tox

          types-dateutil
          types-toml

          nose
          mypy

        ];
        # passthru = {
        #   inherit python;
        #   pythonPath = python.pkgs.makePythonPath propagatedBuildInputs;
        # };


        doCheck = false;
        checkInputs = [
          pytest
        ];
      };
    };
  };
  lenticular-cloud = final.python3.pkgs.lenticular-cloud;
}