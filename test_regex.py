import unittest
import re

regex = r'''(?xim)
    (^.*$\s*)*
    ^(?P<line>\d+):?(?P<col>\d+)?\s*(?P<rule>\w+)?\s*((?P<warning>warning)|(?P<error>error))\s*(?P<message>.+)$\s*
'''


class TestRegex(unittest.TestCase):

    def match_regex_dict(self, str, dict):
        redict = re.compile(regex, re.X).match(str).groupdict()
        self.assertEqual(redict, dict)

    def test_output_with_rule_prepended(self):
        str = '177:24  colors  warning  hexidecimal color should be a variable'
        dict = {
            'line': '177',
            'col': '24',
            'rule': 'colors',
            'warning': 'warning',
            'error': None,
            'message': 'hexidecimal color should be a variable'
        }
        self.match_regex_dict(str, dict)

    def test_output_with_rule_appended(self):
        str = '177:24  warning  hexidecimal color should be a variable  colors'
        dict = {
            'line': '177',
            'col': '24',
            'rule': None,
            'warning': 'warning',
            'error': None,
            'message': 'hexidecimal color should be a variable  colors'
        }
        self.match_regex_dict(str, dict)

    def test_output_with_no_col(self):
        str = '177  warning  hexidecimal color should be a variable'
        dict = {
            'line': '177',
            'col': None,
            'rule': None,
            'warning': 'warning',
            'error': None,
            'message': 'hexidecimal color should be a variable'
        }
        self.match_regex_dict(str, dict)


if __name__ == '__main__':
    unittest.main()
