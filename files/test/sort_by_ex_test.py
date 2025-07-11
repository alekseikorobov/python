import os
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
            
    def test_check_duplicate_file(self):        
            for file_test_name1,content1,file_test_name2,content2,expect_result_check in [
                ('file_test_name1.txt','1234','file_test_name2.txt','1234',True),
                ('file_test_name1.txt','1234','file_test_name2.txt','1235',False),
                ('file_test_name1.txt','1234','file_test_name2.txt','',False),
                ('file_test_name1.txt','','file_test_name2.txt','1234',False),
                
                ('file_test_name1.txt','1234','file_test_name2.txt',None,False),
                ('file_test_name1.txt',None,'file_test_name2.txt','1234',False),
                
                ('file_test_name1.txt',None,'file_test_name2.txt',None,True),
                
                ('file_test_name1.txt','1235','file_test_name2.txt','1234',False),
                ('file_test_name1.txt',','.join(map(str,range(1,10))),'file_test_name2.txt',','.join(map(str,range(1,10))),True),
                ('file_test_name1.txt',','.join(map(str,range(1,1_000_000))),'file_test_name2.txt',','.join(map(str,range(1,1_000_000))),True),
                
                ('file_test_name1.txt',','.join(map(str,range(1,1_000_000))),'file_test_name2.txt',','.join(map(str,range(1,1_000_000,-1))),False),
            ]:
                try:                    
                    with open(file_test_name1,'w') as f1:
                        if content1 is not None:
                            f1.write(content1)
                    with open(file_test_name2,'w') as f2:
                        if content2 is not None:
                            f2.write(content2)
                    
                    result_check = sort_by_ex.check_duplicate_file(file_test_name1,file_test_name2)
                    assert result_check == expect_result_check
                finally:
                    os.remove(file_test_name1)
                    os.remove(file_test_name2)