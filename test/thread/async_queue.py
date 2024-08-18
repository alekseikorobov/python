import asyncio





async def start_reader(queue:asyncio.Queue):
    print(f'start_reader')
    #await asyncio.sleep()
    while True:
        item = await queue.get()
        print(f'{item=}')
    
async def start_writer(queue:asyncio.Queue):
    print(f'start_writer')
    for i in range(3):
        await asyncio.sleep(1)    
        await queue.put(f'element{i}')
    

async def main():
    queue = asyncio.Queue()
    t1 = start_reader(queue)
    t2 = start_writer(queue)
    await asyncio.gather(t1, t2)
    
    

asyncio.run(main())