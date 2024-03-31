import asyncio
from typing import Coroutine, Any
import time


async def baz():
    await asyncio.sleep(5)
    return 'Hello world!'


async def main():
    cor = baz()
    print(cor)
    result = await cor
    print(result)
    return result


if __name__ == '__main__':
    start = time.time()
    r = asyncio.run(main())
    print(r)
    print(time.time()- start)

