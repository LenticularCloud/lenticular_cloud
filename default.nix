{
  pkgs,
  python ? pkgs.python39,
  ...}:
let 
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


  flask-dance = with python.pkgs; buildPythonPackage rec {
    pname = "Flask-Dance";
    version = "5.1.0";
    src = fetchPypi {
      inherit pname version;
      sha256 = "9eb5a404ef1b06a58aabbe5ac496908bda0482af1cf08e8c00188493405842fd";
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
  ory-hydra-client = with python.pkgs; buildPythonPackage rec {
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
    mypy
  ];
}
