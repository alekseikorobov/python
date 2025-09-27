

import unittest
from obsidian import create_note

class TestObsidian(unittest.TestCase):

    def test_validate_url(self):
        urls = [
            ("https://habr.com/ru/articles/837324/",True)
        ]
        for url,except_value in urls:
            result_fact = create_note.validate_url(url)
            assert except_value == result_fact, 'not correct'
            
            
    def test_get_domain_from_url(self):
        urls = [
            ("https://habr.com/ru/articles/837324/",'habr.com'),
            ("https://www.youtube.com/watch?v=e7IWitk9x3o",'youtube.com'),
            ('https://leetcode.com/problems/longest-palindromic-substring/','leetcode.com'),
            ('https://stackoverflow.com/questions/11063458/python-script-to-copy-text-to-clipboard','stackoverflow.com'),
            
            ("http://habr.com/ru/articles/837324/",'habr.com'),
            ("http://www.youtube.com/watch?v=e7IWitk9x3o",'youtube.com'),
            ('http://leetcode.com/problems/longest-palindromic-substring/','leetcode.com'),
            ('http://stackoverflow.com/questions/11063458/python-script-to-copy-text-to-clipboard','stackoverflow.com')
        ]
        for url,except_value in urls:
            result_fact = create_note.get_domain_from_url(url)
            assert except_value == result_fact, f'not correct {except_value=}, {result_fact=}'