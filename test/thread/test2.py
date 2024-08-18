
# put your python code here
import asyncio
async def print_with_delay(n):
    await asyncio.sleep(0.1)
    return f'Coroutine {n} is done'


async def main():
    tasks = [asyncio.create_task(print_with_delay(n)) for n in range(10)]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)
        

asyncio.run(main())