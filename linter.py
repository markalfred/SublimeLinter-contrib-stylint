#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jack Brewer
# Copyright (c) 2015 Jack Brewer
#
# License: MIT

"""Exports the Stylint plugin class."""

from SublimeLinter.lint import NodeLinter, util
from regex import regex


class Stylint(NodeLinter):
    """Provides an interface to stylint."""

    cmd = 'stylint ${temp_file} ${args}'
    defaults = {
        'selector': 'source.stylus, source.stylus.embedded.html',
        '--ignore=,': '',
        '--warn=,': '',
        '--error=,': ''
    }
    regex = regex
    multiline = True
    error_stream = util.STREAM_STDOUT
    tempfile_suffix = 'styl'
