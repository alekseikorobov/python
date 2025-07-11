

import asyncio
import time


async def task1():
    print('start task1')
    #time.sleep(2)
    await asyncio.sleep(2)
    print('done task1')
    
async def task2():
    print('start task2')
    #time.sleep(1)
    await asyncio.sleep(2)
    print('done task2')


async def main():
    t1 = task1()
    t2 = task2()
    # await t1
    # await t2    
    await asyncio.gather(*[t1,t2])
    
asyncio.run(main())
    
    