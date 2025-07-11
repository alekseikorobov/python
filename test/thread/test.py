
# идея создать абстракцию для управления потоками

import asyncio
import time

# class MyActions:
    
#     def __init__(self) -> None:
#         self.waiter
    
async def action1(arg1):    
    print(f'------action1 {arg1=}')
    await asyncio.sleep(2)
    ...

async def action2(arg1):
    print(f'action2 {arg1=}')
    await asyncio.sleep(1)
    ...

async def main():
    for arg1 in [1,2,3,4,5,6,8,9,10]:
        tasks = []       
        if arg1 in [5,8]:
            task1 = asyncio.create_task(action1(arg1))
            tasks.append(task1)

        task2 = asyncio.create_task(action2(arg1))
        tasks.append(task2)
        asyncio.gather(*tasks)


asyncio.run(main())
