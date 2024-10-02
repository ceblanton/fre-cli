Installation
=====

Generic
----------
fre-cli is conda-installable on Linux environments. To install it and dependencies into a environment called ``fre``, run::

$ conda create --name fre --channel noaa-gfdl fre-cli

Then activate the newly created environment::

$ conda activate fre

(fre)> fre --help

Usage: fre [OPTIONS] COMMAND [ARGS]...

  'fre' is the main CLI click group that houses the other tool groups as
  lazy subcommands.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  app         - access fre app subcommands
  catalog     - access fre catalog subcommands
  check       - access fre check subcommands
  cmor        - access fre cmor subcommands
  list        - access fre list subcommands
  make        - access fre make subcommands
  pp          - access fre pp subcommands
  run         - access fre run subcommands
  test        - access fre test subcommands
  yamltools   - access fre yamltools subcommands

GFDL
----------
If you are at GFDL (workstations or PP/AN), fre-cli is already installed and can be loaded as an Environment Module.

Modules in the format "fre/YYYY.NN[.PP]" are versions of fre-cli corresponding to the tags on github,
where YYYY is the year of the release, NN is a two-digit incrementing integar, and PP is an optional patch release.

e.g.

> module avail fre

--------------------------------------- /home/fms/local/modulefiles ------------------------------------
fre/2024.00        fre/2024.01   fre/test
fre/bronx-21       fre/bronx-22  fre/canopy-dualpp

> module load fre/2024.01

Loading fre/canopy
  Loading requirement: zlib/1.2.13 hdf5/1.14.1-2 netcdf-c/4.9.2 nccmp/1.9.0.1 gsl/2.7.1 udunits/2.2.28 nco/5.1.5 perlbrew/5.38.2 gcp/2.3 hsm/1.3.0 fre-nctools/2023.01.02

>fre --help

Usage: fre [OPTIONS] COMMAND [ARGS]...

  'fre' is the main CLI click group that houses the other tool groups as
  lazy subcommands.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  app         - access fre app subcommands
  catalog     - access fre catalog subcommands
  check       - access fre check subcommands
  cmor        - access fre cmor subcommands
  list        - access fre list subcommands
  make        - access fre make subcommands
  pp          - access fre pp subcommands
  run         - access fre run subcommands
  test        - access fre test subcommands
  yamltools   - access fre yamltools subcommands
