import re
from formating_date import formating
import unittest

class TestFormatingDt(unittest.TestCase):
    
    def test_formating(self):        
        assert formating('2020-09-01 12-04-51')[0]=='2020-09-01 12-04-51'
        assert formating('2020-09-01 12-04-52.123')[0]=='2020-09-01 12-04-52'
        assert formating('2020+09+01 12+04+52')[0]=='2020-09-01 12-04-52'
        assert formating('2020+09+01 12+04+52.123')[0]=='2020-09-01 12-04-52'
        assert formating('1900+01+01 12+12+12')[0] is None
        assert formating('01-09-2020 12-04-51')[0]=='01-09-2020 12-04-51'

        assert formating('2020-09-01 12-04')[0]=='2020-09-01 12-04'
        assert formating('2020+09+01 12+04')[0]=='2020-09-01 12-04'
        assert formating('2020+09+01 12+04')[0]=='2020-09-01 12-04'
        assert formating('1900+01+01 12+12')[0] is None
        assert formating('01-09-2020 12-04')[0]=='01-09-2020 12-04'


        assert formating('2020-9-1 12-04-51')[0]=='2020-09-01 12-04-51'
        assert formating('2020-9-1 12-04-52.123')[0]=='2020-09-01 12-04-52'
        assert formating('2020+9+1 12+04+52')[0]=='2020-09-01 12-04-52'
        assert formating('2020+9+1 12+04+52.123')[0]=='2020-09-01 12-04-52'
        assert formating('1900+1+1 12+12+12')[0] is None
        assert formating('1-9-2020 12-04-51')[0]=='01-09-2020 12-04-51'

        assert formating('2020-9-1 12-04')[0]=='2020-09-01 12-04'
        assert formating('2020+9+1 12+04')[0]=='2020-09-01 12-04'
        assert formating('2020+9+1 12+04')[0]=='2020-09-01 12-04'
        assert formating('1900+1+1 12+12')[0] is None
        assert formating('1-9-2020 12-04')[0]=='01-09-2020 12-04'


        assert formating('1/27/2025 12:04')[0]=='2025-01-27 12-04'
        assert formating('1/27/2025')[0]=='2025-01-27'
        assert formating('1/27/1950')[0] is None
        assert formating('1/27/2025 12:04 PM')[0]=='2025-01-27 12-04'
        assert formating('1/27/2025 12:04:04')[0]=='2025-01-27 12-04-04'
        
        for f,ex in [
            ('20180106_181731','2018-01-06 18-17-31'),
            ('20180106 181731','2018-01-06 18-17-31'),
            ('20180106181731','2018-01-06 18-17-31'),
            ('20180106','2018-01-06'),
            ('20180106____уке','2018-01-06'),
        ]:
            result,_ = formating(f)
            assert result==ex, f'{result=}'
        
        

        
