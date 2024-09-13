''' tests for fre.cmor._cmor_run_subtool '''
import subprocess
import datetime
import pathlib
from pathlib import Path
from datetime import date

import fre
from fre import cmor
from fre.cmor import _cmor_run_subtool

# where are we? we're running pytest from the base directory of this repo
rootdir = 'fre/tests/test_files'

# explicit inputs to tool
indir = f'{rootdir}/ocean_sos_var_file'
varlist = f'{rootdir}/varlist'
table_config = f'{rootdir}/cmip6-cmor-tables/Tables/CMIP6_Omon.json'
exp_config = f'{rootdir}/CMOR_input_example.json'
outdir = f'{rootdir}/outdir'

# determined by cmor_run_subtool
YYYYMMDD=date.today().strftime('%Y%m%d')
cmor_creates_dir='CMIP6/CMIP6/ISMIP6/PCMDI/PCMDI-test-1-0/piControl-withism/r3i1p1f1/Omon/sos/gn'
# why does this have "fre" at the end of it?
full_outputdir = \
   f"{outdir}fre/{cmor_creates_dir}/v{YYYYMMDD}"
full_outputfile=f"{full_outputdir}/sos_Omon_PCMDI-test-1-0_piControl-withism_r3i1p1f1_gn_199307-199807.nc"

# FYI
filename = 'ocean_monthly_1x1deg.199301-199712.sos.nc' # unneeded, this is mostly for reference
full_inputfile=f"{indir}/{filename}"




def test_fre_cmor_run(capfd):
    ''' fre cmor run, test-use case '''

    # clean up, lest we fool outselves
    if Path(full_outputfile).exists():
        Path(full_outputfile).unlink()

    fre.cmor._cmor_run_subtool(
        indir = indir,
        varlist = varlist,
        table_config = table_config,
        exp_config = exp_config,
        outdir = outdir
    )
    # success condition tricky... tool doesnt return anything really... ?
    # TODO think about returns and success conditions
    assert all( [ Path(full_outputfile).exists(),
                  Path(full_inputfile).exists() ] )
    out, err = capfd.readouterr()

def test_fre_cmor_run_output_compare(capfd):
    ''' I/O comparison of prev test-use case '''
    print(f'full_outputfile={full_outputfile}')
    print(f'full_inputfile={full_inputfile}')

    nccmp_cmd= [ "nccmp", "-f", "-m", "-g", "-d",
                 f"{full_inputfile}",
                 f"{full_outputfile}"    ]
    print(f"via subprocess, running {' '.join(nccmp_cmd)}")
    result = subprocess.run( ' '.join(nccmp_cmd),
                             shell=True,
                             check=False
                          )
    #subprocess.run(["rm", "-rf", f"{outdir}/CMIP6/CMIP6/"])
    assert result.returncode == 1
    out, err = capfd.readouterr()
