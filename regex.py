"""
The base regex used to parse Stylint warnings and errors.

It is exported here for use by the linter and the tests.
"""

regex = r'''
    (?xim)
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
