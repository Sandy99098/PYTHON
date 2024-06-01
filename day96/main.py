import asyncio

async def func1():
    await asyncio.sleep(1)
    print("This is function 1")

async def func2():
    await asyncio.sleep(1)
    print("This is function 2")

async def func3():
    await asyncio.sleep(4)
    print("This is function 3")

async def main():
    # Create tasks to run functions concurrently
    # task1 = asyncio.create_task(func1())
    # task2 = asyncio.create_task(func2())
    # task3 = asyncio.create_task(func3())
    
    #  to run all the function s concurrently 
    L = await asyncio.gather( func1(),func2(),func3())
    
    
    # Wait for all tasks to complete
    # await task1
    # await task2
    # await task3
    
    
    # print(L)
    

asyncio.run(main())
