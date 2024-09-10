#!/usr/bin/python3

import os
import sys
from pathlib import Path
import click
from .gfdlfremake import makefilefre, varsfre, targetfre, yamlfre
import fre.yamltools.combine_yamls as cy 

@click.command()
def makefile_create(yamlfile,platform,target):
    srcDir="src"
    checkoutScriptName = "checkout.sh"
    baremetalRun = False # This is needed if there are no bare metal runs
    ## Split and store the platforms and targets in a list
    plist = platform
    tlist = target
    yml = yamlfile
    name = yamlfile.split(".")[0]

    ## If combined yaml does not exist, combine model, compile, and platform yamls
    cd = Path.cwd()
    combined = Path(f"combined-{name}.yaml")
    combined_path=os.path.join(cd,combined)

    # Combine model, compile, and platform yamls
    # If fre yammltools combine-yamls tools was used, the combined yaml should exist
    if Path(combined_path).exists():
        full_combined = combined_path
        print("\nNOTE: Yamls previously merged.")
    else:
        comb = cy.init_compile_yaml(yml,platform,target)
        full_combined = cy.get_combined_compileyaml(comb)

    ## Get the variables in the model yaml
    freVars = varsfre.frevars(full_combined)
 
    ## Open the yaml file and parse as fremakeYaml
    modelYaml = yamlfre.freyaml(full_combined,freVars)
    fremakeYaml = modelYaml.getCompileYaml()

    fremakeBuildList = []
    ## Loop through platforms and targets
    for platformName in plist:
        for targetName in tlist:
            targetObject = targetfre.fretarget(targetName)
            if modelYaml.platforms.hasPlatform(platformName):
                pass
            else:
                raise ValueError (platformName + " does not exist in " + modelYaml.combined.get("compile").get("platformYaml"))

            (compiler,modules,modulesInit,fc,cc,modelRoot,iscontainer,mkTemplate,containerBuild,ContainerRun,RUNenv)=modelYaml.platforms.getPlatformFromName(platformName)

  ## Make the bldDir based on the modelRoot, the platform, and the target
            srcDir = modelRoot + "/" + fremakeYaml["experiment"] + "/src"
            ## Check for type of build
            if iscontainer == False:
                baremetalRun = True
                bldDir = modelRoot + "/" + fremakeYaml["experiment"] + "/" + platformName + "-" + targetObject.gettargetName() + "/exec"
                os.system("mkdir -p " + bldDir)
                ## Create the Makefile
                freMakefile = makefilefre.makefile(exp = fremakeYaml["experiment"],
                                             libs = fremakeYaml["baremetal_linkerflags"],
                                             srcDir = srcDir,
                                             bldDir = bldDir,
                                             mkTemplatePath = mkTemplate)
                # Loop through components and send the component name, requires, and overrides for the Makefile
                for c in fremakeYaml['src']:
                    freMakefile.addComponent(c['component'],c['requires'],c['makeOverrides'])
                freMakefile.writeMakefile()
                click.echo("\nMakefile created at " + bldDir + "/Makefile" + "\n")
            else:
                image="ecpe4s/noaa-intel-prototype:2023.09.25"
                bldDir = modelRoot + "/" + fremakeYaml["experiment"] + "/exec"
                tmpDir = "tmp/"+platformName
                freMakefile = makefilefre.makefileContainer(exp = fremakeYaml["experiment"],
                                                      libs = fremakeYaml["container_addlibs"],
                                                      srcDir = srcDir,
                                                      bldDir = bldDir,
                                                      mkTemplatePath = mkTemplate,
                                                      tmpDir = tmpDir)

                # Loop through compenents and send the component name and requires for the Makefile
                for c in fremakeYaml['src']:
                    freMakefile.addComponent(c['component'],c['requires'],c['makeOverrides'])
                freMakefile.writeMakefile()
                click.echo("\nMakefile created at " + bldDir + "/Makefile" + "\n")

if __name__ == "__main__":
    makefile_create()
