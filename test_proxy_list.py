import contextlib
import aiohttp
import asyncio
from typing import Dict
from actions import cleanJson, selectedCountryProxies
from aiohttp_socks import ProxyConnector

working_proxies: list = []
with open("socks5_proxies.txt", "r") as f:
    proxies = f.read().strip().split("\n")
    # proxies = f_read

    
async def test_proxy(proxy: str):
    proxy_url = f"socks5://{proxy}"
    connector = ProxyConnector.from_url(proxy_url)
    async with aiohttp.ClientSession(connector=connector) as session:
        with contextlib.suppress(Exception):
            async with session.get('https://httpbin.org/ip') as response:
                # print(f"{proxy_name} is working! IP: {await response.text()}")
                working_proxies.append(proxy)

async def test_proxies(proxies: list):
    tasks = []
    for proxyy in proxies:
        tasks.append(asyncio.ensure_future(test_proxy(proxyy)))
    print("Started Async Gather.")
    await asyncio.gather(*tasks)
    print("Async Gather is done.")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_proxies(proxies))
    loop.close()
    for p_proxy in working_proxies: print(p_proxy)