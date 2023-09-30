{
  description = "Lenticular cloud interface";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
    flake-compat = { # for shell.nix
      url = "github:edolstra/flake-compat";
      flake = false;
    };
    nix-node-package = {
      url = "github:mkg20001/nix-node-package";
      flake = false;
    };
  };
  outputs = { self, nixpkgs, nix-node-package, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system}.extend (import ./overlay.nix);
    in rec {
      formatter = pkgs.nixpkgs-fmt;
      devShells.default = pkgs.python3.withPackages (ps: (
        pkgs.lenticular-cloud.propagatedBuildInputs ++
        pkgs.lenticular-cloud.testBuildInputs
      ));

      packages.default = pkgs.lenticular-cloud;

      checks = {
        package = packages.default;
        devShells = devShells.default;
      };
    }) // {
      nixosModules = {
        default = import ./module.nix;
      };
      overlays.default = import ./overlay.nix;
      nixosConfigurations.testSystem = nixpkgs.lib.nixosSystem {
        system = "x86_64-linux";
        modules = [
          self.nixosModules.default
          "${nixpkgs}/nixos/modules/virtualisation/qemu-vm.nix"
        ];
      };
    };
}
