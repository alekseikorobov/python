import asyncio


class MyRequest:
    def __init__(self):
        self.proxys = [
            i for i in range(10)
        ]
        
        self.tasks= {
            proxy:() for proxy in self.proxys
        }
        
        self.proxys
    
    async def fw(self,proxy):
        async def get(url):
            return None
        return get
    
    def get_avaliable_task(self):
        
    
    async def get(self,url):
        task = self.get_avaliable_task()
        await task(url)
                


urls = [
    f'https://example.com/{i}' for i in range(100)
]


mr = MyRequest()


for url in urls:
    mr.get(url)
    
    