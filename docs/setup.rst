Setup
=====

Generic
----------
Need to set up Conda environment first and foremost

If on workstation:
module load conda

Create new Conda environment
conda create -n [environmentName]

Append necessary channels
conda config --append channels noaa-gfdl
conda config --append channels conda-forge

Run conda install on needed dependencies
conda install noaa-gfdl::fre-cli should install the CLI package located at https://anaconda.org/NOAA-GFDL/fre-cli created from the meta.yaml file

All other dependencies used by the tools are installed along with this install (configured inside the meta.yaml), with the exception of local modules
setup.py file allows fre.py to be ran with fre as the entry point on the command line instead of python fre.py

Enter commands and follow --help messages for guidance (brief rundown of commands also provided below)

If the user just runs fre, it will list all the command groups following fre, such as run, make, pp, etc. and once the user specifies a command group, the list of available subcommands for that group will be shown

Commands that require arguments to run will alert user about missing arguments, and will also list the rest of the optional parameters if --help is executed

Argument flags are not positional, can be specified in any order as long as they are specified

Can run directly from any directory, no need to clone repository

May need to deactivate environment and reactivate it in order for changes to apply

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
