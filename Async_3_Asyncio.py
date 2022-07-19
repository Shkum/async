import asyncio
from time import time


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.5)

# @asyncio.coroutine  #  old style before python 3.5
async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f'{count} seconds have passed')
        count += 1
        await asyncio.sleep(1)


async def main():
    # task1 = asyncio.ensure_future(print_nums())  #  old style before python 3.5
    # task2 = asyncio.ensure_future(print_time())
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(main())
    # loop = asyncio.get_event_loop()  #  old style before python 3.5
    # loop.run_until_complete(main())
    # loop.close()

