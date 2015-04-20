#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jack Brewer
# Copyright (c) 2015 Jack Brewer
#
# License: MIT
#

"""This module exports the Stylint plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Stylint(NodeLinter):

    """Provides an interface to stylint."""

    npm_name = 'stylint'
    syntax = 'stylus'
    cmd = 'stylint @ *'
    executable = 'stylint'
    version_requirement = '>= 0.9.3'
    regex = r'''(?xi)
        # Comments show example output for each line of a Stylint warning
        # 'Near' can contain trailing whitespace, which we avoid capturing

        # Warning:  commas must be followed by a space for readability
        ^((?P<warning>warning)|(?P<error>Error)):\s*(?P<message>.+)$\s*
        # File: /path/to/file/example.styl
        ^.*$\s*
        # Line: 46: color rgba(0,0,0,.5)
        ^Line:\s*(?P<line>\d+):\s*(?P<near>.*\S)
    '''
    multiline = True
    error_stream = util.STREAM_STDOUT
    tempfile_suffix = 'styl'
    config_file = ('--config', '.stylintrc', '~')
