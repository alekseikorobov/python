
import time
from functools import wraps
import tracemalloc
from time import perf_counter 

class MyTimer:

    def __init__(self):        
        #self.start_time = time.time()        
        tracemalloc.start()
        self.start_time = perf_counter()

    def __enter__(self):
        pass

    def __exit__(self, *args):
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()        
        print(f'Memory usage:\t\t {current / 10**6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10**6:.6f} MB ')
        print(f'Time elapsed is seconds: {finish_time - self.start_time:.6f}')
        print(f'{"-"*40}')
        tracemalloc.stop()


#https://www.freecodecamp.org/news/python-decorators-explained-with-examples/
def measure_performance(func):
    '''Measure performance of a function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print()
        with MyTimer() as _:
            return func(*args, **kwargs)
            #print()
        
    return wrapper