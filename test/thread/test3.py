import asyncio
# Counter_1 - имя счётчика
# 13 - максимальное значение для счётчика Counter_1 

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

counters = {}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}

async def counter(name:str,sleep:int):
    global counters
    while counters[name] < max_counts[name]:
        counters[name] += 1
        print(f'{name}: {counters[name]}')
        await asyncio.sleep(sleep)
        

async def main():
    global counters
    
    counters = {name:0 for name in max_counts}
    
    tasks = [asyncio.create_task(counter(name,delays[name])) for name in max_counts]
    await asyncio.gather(*tasks)
    
    
asyncio.run(main())