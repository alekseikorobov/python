
import unittest
import moving_file.sort_by_ex as sort_by_ex

class MyTest(unittest.TestCase):
    
    def test_sort_file_by_exts(self):
        for index,(files,ext,exp_files) in enumerate([
            (['file1.txt'],'.tx',[]),
            (['file1.txt'],'.xt',[]),
            (['file1.txt'],'.txt',['file1.txt']),
            (['file1.txt','file2.md','file3.TXT',],'.txt',['file1.txt', 'file3.TXT']),
            (['file1.txt','file2.md','file3.json','file4.TXT','file5.json',],'.txt,.json',['file1.txt','file3.json', 'file4.TXT','file5.json'])
        ],start=1):
            files_result = sort_by_ex.sort_file_by_exts(files,ext)
            assert files_result == exp_files, f"[{index}]:{files=},{ext=},{files_result=},{exp_files=}"
            
    def test_sort_file_by_exts_not(self):
        for index,(files,ext,exp_files) in enumerate([
            (['file1.txt'],'.tx',['file1.txt']),
            (['file1.txt'],'.xt',['file1.txt']),
            (['file1.txt'],'.txt',[]),
            (['file1.txt','file2.md','file3.TXT',],'.txt',['file2.md']),
            (['file1.txt','file2.md','file3.json','file4.TXT','file5.json',],'.txt,.json',['file2.md'])
        ], start=1):
            files_result = sort_by_ex.sort_file_by_exts(files,ext,reverse=True)
            assert files_result == exp_files, f"[{index}]:{files=},{ext=},{files_result=},{exp_files=}"
  