{
  description = "Lenticular cloud interface";
  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    flake-compat = { # for shell.nix
      url = "github:edolstra/flake-compat";
      flake = false;
    };
    nix-node-package = {
      url = "github:mkg20001/nix-node-package";
      flake = false;
    };
    tuxpkgs = {
      url = "git+ssh://git@git.o-g.at/nixpkg/tuxpkgs.git";
      inputs.nixpkgs.follows = "nixpkgs";
      inputs.flake-utils.follows = "flake-utils";
    };
  };
  outputs = { self, nixpkgs, nix-node-package, flake-utils, tuxpkgs, ... }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system}.extend (import ./overlay.nix);
    in rec {
      formatter = pkgs.nixpkgs-fmt;
      devShells.default = pkgs.mkShell {packages = [
         (pkgs.python3.withPackages (ps: (
          pkgs.lenticular-cloud.propagatedBuildInputs ++
          pkgs.lenticular-cloud.testBuildInputs
        )))
      ];};

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
          tuxpkgs.nixosModules.ory-hydra
          "${nixpkgs}/nixos/modules/virtualisation/qemu-vm.nix"
          ({...}:{
            security.acme.acceptTerms = true;
            security.acme.defaults.email = "acme@example.com";
            services.lenticular-cloud = {
              enable = true;
              domain = "example.com";
            };
            services.ory-hydra = {
              enable = true;
              admin_domain = "admin-hydra.local";
            };
            networking.hosts = {"::1" = [ "admin-hydra.local" ]; };
            services.getty.autologinUser = "root";
            virtualisation.qemu.options = ["-vga none"];
          })
        ];
      };
    };
}
