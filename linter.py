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


class Stylint(NodeLinter):

    """Provides an interface to stylint."""

    npm_name = 'stylint'
    cmd = 'stylint @ *'
    executable = 'stylint'
    version_requirement = '>= 1.5.0'
    defaults = {
        'selector': 'source.stylus, text.html.vue',
        '--ignore=,': '',
        '--warn=,': '',
        '--error=,': ''
    }
    regex = r'''
        (?xi)
        # Comments show example output for each line of a Stylint warning
        # /path/to/file/example.styl
        (^.*$\s*)*
        # 177:24  colors  warning  hexidecimal color should be a variable
        # 177:24  warning  hexidecimal color should be a variable  colors
        # 177  warning  hexidecimal color should be a variable  colors
        ^
        ((?P<filename>\S+)\s+)?
        (?P<line>\d+)
        :?
        (?P<col>\d+)?
        \s*
        (?P<rule>\w+)?
        \s*
        ((?P<warning>warning)|(?P<error>error))
        \s*
        (?P<message>.+)
        $\s*
    '''
    multiline = True
    error_stream = util.STREAM_STDOUT
    tempfile_suffix = 'styl'
    config_file = ('--config', '.stylintrc', '~')
