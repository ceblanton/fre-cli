#!/usr/bin/python3

#import fremake
import make.varsfre
import make.platformfre
import make.yamlfre
import make.targetfre
import make.buildBaremetal
from multiprocessing.dummy import Pool
import logging
import os
import click

@click.command()

def compile_create(yamlfile,platform,target,jobs,parallel,verbose):
    # Define variables
    yml = yamlfile
    ps = platform
    ts = target
    nparallel = parallel
    jobs = str(jobs)

    if verbose:
      logging.basicCOnfig(level=logging.INFO)
    else:
      logging.basicConfig(level=logging.ERROR)

    srcDir="src"
    checkoutScriptName = "checkout.sh"
    baremetalRun = False # This is needed if there are no bare metal runs

    ## Split and store the platforms and targets in a list
    plist = platform
    tlist = target

    ## Get the variables in the model yaml
    freVars = make.varsfre.frevars(yml)

    ## Open the yaml file and parse as fremakeYaml
    modelYaml = make.yamlfre.freyaml(yml,freVars)
    fremakeYaml = modelYaml.getCompileYaml()

    ## Error checking the targets
    for targetName in tlist:
         target = make.targetfre.fretarget(targetName)

    fremakeBuildList = []
    ## Loop through platforms and targets
    for platformName in plist:
      for targetName in tlist:
         target = make.targetfre.fretarget(targetName)
         if modelYaml.platforms.hasPlatform(platformName):
              pass
         else:
              raise SystemExit (platformName + " does not exist in " + modelYaml.platformsfile)
         (compiler,modules,modulesInit,fc,cc,modelRoot,iscontainer,mkTemplate,containerBuild,ContainerRun,RUNenv)=modelYaml.platforms.getPlatformFromName(platformName)
    ## Make the bldDir based on the modelRoot, the platform, and the target
         srcDir = modelRoot + "/" + fremakeYaml["experiment"] + "/src"
         ## Check for type of build
         if iscontainer == False:
              baremetalRun = True
              bldDir = modelRoot + "/" + fremakeYaml["experiment"] + "/" + platformName + "-" + target.gettargetName() + "/exec"
              os.system("mkdir -p " + bldDir)
              ## Create a list of compile scripts to run in parallel
              fremakeBuild = make.buildBaremetal.buildBaremetal(fremakeYaml["experiment"],mkTemplate,srcDir,bldDir,target,modules,modulesInit,jobs)
              for c in fremakeYaml['src']:
                   fremakeBuild.writeBuildComponents(c) 
              fremakeBuild.writeScript()
              fremakeBuildList.append(fremakeBuild)

    if baremetalRun:
        pool = Pool(processes=nparallel)                         # Create a multiprocessing Pool
        pool.map(make.buildBaremetal.fremake_parallel,fremakeBuildList)  # process data_inputs iterable with pool 


#def compile_run():
#  ## Run the build
#  fremakeBuild.run()

if __name__ == "__main__":
    compile_create()
