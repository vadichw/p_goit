import asyncio
import platform
import logging
from pprint import pprint

import aiohttp


async def request(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    r = await response.json()
                    return r
                logging.error(f"Error status {response.status} for {url}")
        except aiohttp.ClientConnectorError as e:
            logging.error(f"Connection error {url}: {e}")
        return None


async def get_exchange():
    res = await request('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
    return res


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(get_exchange())
    pprint(r)
