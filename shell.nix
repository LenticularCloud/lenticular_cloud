{
  pkgs ? import <nixpkgs> {},
  python ? pkgs.python39
}:
let
  settings = import ./default.nix {inherit pkgs python;};
in
pkgs.mkShell {
    # nativeBuildInputs is usually what you want -- tools you need to run
    nativeBuildInputs = settings.nativeBuildInputs ++ settings.testBuildInputs ++ [ pkgs.nodePackages.npm pkgs.nodejs python.pkgs.build ];
}

