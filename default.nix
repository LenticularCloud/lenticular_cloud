{
  pkgs,
  python ? pkgs.python310,
  nodejs ? pkgs.nodejs,
  ...}:
let 
  nixNodePackage = builtins.fetchGit {
    url = "https://github.com/mkg20001/nix-node-package.git";
    rev = "03285e212016db5f28530563b58cfcc5706ff73f";
  };
  makeNode = import "${nixNodePackage}/nix/default.nix" pkgs {
    root = ./.;
    install = false;
    nodejs = nodejs;
  };
  node-env = makeNode { };

  urlobject = with python.pkgs; buildPythonPackage rec {
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

  python_attrs = with python.pkgs; buildPythonPackage rec {
    pname = "attrs";
    version = "21.4.0";
    src = fetchPypi {
      inherit pname version;
      sha256 = "626ba8234211db98e869df76230a137c4c40a12d72445c45d5f5b716f076e2fd";
    };
    #doCheck = true;
    doCheck = false;
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
  ldap3-orm = with python.pkgs; buildPythonPackage rec {
    pname = "ldap3-orm";
    version = "2.7.0";
    src = fetchPypi {
      inherit pname version;
      sha256 = "8783886d4ce90d66da61ce24619593a265b50f0de1fbebe86df95c6788661664";
    };
    doCheck = false;
    propagatedBuildInputs = [
      ldap3
      six
    ];

  };
  u2flib-server = {};
  ory-hydra-client-old = with python.pkgs; buildPythonPackage rec {
    pname = "ory-hydra-client";
    version = "1.10.6";
    src = fetchPypi {
      inherit pname version;
      sha256 = "57f877e55a8f202db27f5cbae9c55a1b1a91848ef46d0cbd3b710ef77882095c";
    };
    doCheck = false;
    propagatedBuildInputs = [
      urllib3
      python-dateutil
    ];
  };
  ory-hydra-client = with python.pkgs; buildPythonPackage rec {
    pname = "ory-hydra-client";
    version = "1.9.2";
    src = ./libs/ory-hydra-client; 
#    doCheck = false;
    propagatedBuildInputs = [
      urllib3
      python-dateutil
      #python_attrs
      attrs
      httpx
    ];
  };
in
{
  nativeBuildInputs = with python.pkgs; [
      flask
      flask-restful
      flask_sqlalchemy
      flask_wtf
      flask-babel
      flask_login
      requests
      requests_oauthlib
      ldap3
      ldap3-orm
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

#python-u2flib-server


#flask-debug

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
}
