import unittest
import re
from regex import regex

class TestRegex(unittest.TestCase):

    def match_regex_dict(self, str, dict):
        redict = re.compile(regex, re.X).match(str).groupdict()
        self.assertEqual(redict, dict)

    def test_output_with_rule_prepended(self):
        str = '177:24  colors  warning  hexidecimal color should be a variable'
        dict = {
            'filename': None,
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
            'filename': None,
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
            'filename': None,
            'line': '177',
            'col': None,
            'rule': None,
            'warning': 'warning',
            'error': None,
            'message': 'hexidecimal color should be a variable'
        }
        self.match_regex_dict(str, dict)

    def test_multiline_output(self):
        str = '/path/to/file/example.styl\n\n31:10 colons error missing colon between property and value'
        dict = {
            'filename': None,
            'line': '31',
            'col': '10',
            'rule': 'colons',
            'warning': None,
            'error': 'error',
            'message': 'missing colon between property and value'
        }
        self.match_regex_dict(str, dict)

    def test_prepended_filename(self):
        str = '/path/to/file/example.styl 31:10 colons error missing colon between property and value'
        dict = {
            'filename': '/path/to/file/example.styl',
            'line': '31',
            'col': '10',
            'rule': 'colons',
            'warning': None,
            'error': 'error',
            'message': 'missing colon between property and value'
        }
        self.match_regex_dict(str, dict)


if __name__ == '__main__':
    unittest.main()
