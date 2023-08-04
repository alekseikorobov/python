
# сравнение методов чтения больших файлов
# цель - научиться читать большие файлы самым быстрым способом


#https://stackoverflow.com/questions/26127889/python-read-stream

import os
#from . my_timer import MyTimer,measure_performance

source_file = 'file_res.txt'

# with MyTimer() as _:
#     with open(source_file,'r') as source:
#         res = source.read()
# print(f'{len(res)=}')

# with MyTimer() as _:
#     s = os.path.getsize(source_file)
# print(f'{s=}')


# import io
# with MyTimer() as _:
#     f = io.open(source_file)
#     while True:
#         f.readline()

# with MyTimer() as _:
#     count_line = 0
#     with open(source_file,'r') as source:
#         while True:
#             count_line += 1
#             line = source.readline()
#             if not line:
#                 break
# print(f'{count_line=}')

def blocks(files, size=65536):
    while True:
        b = files.read(size)
        if not b: break
        yield b

# bast method!!!
# time executed - 2.25 second
# with MyTimer() as _:
#     with open(source_file, "r",encoding="utf-8",errors='ignore') as f:
#         print(sum(bl.count("\n") for bl in blocks(f)))
        
        
# import mmap
# #time executed - 96.77 second
# def mapcount(filename):
#     with open(filename, "r+") as f:
#         buf = mmap.mmap(f.fileno(), 0)
#         lines = 0
#         readline = buf.readline
#         while readline():
#             lines += 1
#         return lines
    
# with MyTimer() as _:
#     mapcount(source_file)

# @measure_performance
# def test_function():    
#     with open(source_file, "r",encoding="utf-8",errors='ignore') as f:
#         print(sum(bl.count("\n") for bl in blocks(f)))
    
# test_function()