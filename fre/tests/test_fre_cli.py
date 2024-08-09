#!/usr/bin/env python3

# tests are structured in the manner of:
# https://click.palletsprojects.com/en/8.1.x/testing/
# general intent is to test the cli of each (sub)tool
# command, help, command does not exist

from click.testing import CliRunner
runner = CliRunner()

from fre import fre

# tests for base 'fre' calls

def test_cli_fre():
    result = runner.invoke(fre.fre)
    assert result.exit_code == 0

def test_cli_fre_help():
    result = runner.invoke(fre.fre, args='--help')
    assert result.exit_code == 0

def test_cli_fre_option_dne():
    result = runner.invoke(fre.fre, args='optionDNE')
    assert result.exit_code == 2



    
