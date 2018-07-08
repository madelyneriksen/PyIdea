#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyidea` package."""

import pytest

from click.testing import CliRunner

from pyidea import pyidea
from pyidea import cli


def test_help_and_entry():
    """
    Test that the command line can be launched, that --help
    returns exit code zero, and that the project basic structure
    is correct.
    """
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0

def test_new_idea():
    """
    Main usage is to test that valid parameters are accepted,
    and return an exit code of zero.

    Also test that incorrect parameters that are passed to make
    Ideas do not succeed. In general usage, this should never occur,
    however it might if the script is entered in a non-standard way.
    """
    runner = CliRunner()
    valid_idea = runner.invoke(cli.main, ["--new", "Make A Cool Thing"])
    assert valid_idea.exit_code == 0
    assert "Idea saved!" in valid_idea.output
    invalid_idea = runner.invoke(cli.main, ["--new"])
    assert invalid_idea.exit_code == 2
    assert "requires an argument" in invalid_idea.output

def test_list_ideas():
    """
    Make sure listing ideas works properly.
    """
    runner = CliRunner()
    valid_show = runner.invoke(cli.main, ['--show'])
    assert valid_show.exit_code == 0

def test_complete_ideas():
    """
    Test that nonexistant ideas can't get completed
    """
    runner = CliRunner()
    invalid_complete = runner.invoke(cli.main, ["--complete", -1])
    assert invalid_complete.exit_code == 2

def test_idea_format():
    """
    Test that a string can be made into an idea, and
    is formatted properly for using in PeeWee.
    """
    assert pyidea.create_idea("Cool Idea") == {"text": "Cool Idea"}
