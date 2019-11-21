# coding:utf-8

import asyncio


async def coroutine_example():
    await asyncio.sleep(2)
    print("end")



coro = coroutine_example()
loop = asyncio.get_event_loop()
print("1")
loop.run_until_complete(coro)
print("2")
loop.close()