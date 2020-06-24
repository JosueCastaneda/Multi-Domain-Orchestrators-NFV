import asyncio
import time


async def factorial(name, number):
    f = 1
    if number == 2:
        await asyncio.sleep(1)
        print('Extra time')
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def non_concurrents():
    print(f"started at {time.strftime('%X')}")
    await factorial("A", 2)
    await factorial("B", 3)
    await factorial("C", 4)
    print(f"finished at {time.strftime('%X')}")

async def task_time():
    print(f"started at {time.strftime('%X')}")
    # Task concurrents
    task1 = asyncio.create_task(factorial("A", 2))
    task2 = asyncio.create_task(factorial("B", 3))
    task3 = asyncio.create_task(factorial("C", 4))
    # asyncio.run(task1)
    # asyncio.run(task2)
    # asyncio.run(task3)
    await task1
    await task2
    await task3
    print(f"finished at {time.strftime('%X')}")

async def gather_concurrent():
    print(f"started at {time.strftime('%X')}")
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

    print(f"finished at {time.strftime('%X')}")

async def main():
    # await non_concurrents()
    await task_time()
    # await gather_concurrent()

asyncio.run(main())