import asyncio, aiohttp
from typing import Dict
from main import apiRespList
from contextlib import suppress
from aiohttp_socks import ProxyConnector
from actions import cleanJson, writeJson, selectedCountryProxies

writeJson(apiRespList)  # Write into APIProxy.json
selectedCountryProxies()  # Write into proxy.json

cleanJson("proxy.json")
proxies: dict = selectedCountryProxies()
working_proxies: dict = {}
async def json_test_proxy(proxy_name: str, proxy: Dict[str, str]):
    proxy_url = f"socks5://{proxy['Proxy']}"
    connector = ProxyConnector.from_url(proxy_url)
    async with aiohttp.ClientSession(connector=connector) as session:
        with suppress(Exception):
            async with session.get('https://httpbin.org/ip') as response:
                working_proxies[proxy_name] = proxy

async def json_test_proxies(proxies: Dict[str, Dict[str, str]]):
    tasks = []
    for proxy_name, proxy in proxies.items():
        tasks.append(asyncio.ensure_future(json_test_proxy(proxy_name, proxy)))
    print("Started testing Socks5 proxies")
    await asyncio.gather(*tasks)
    print("Ended testing Socks5 proxies\n")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(json_test_proxies(proxies))
    loop.close()
    for p_name, p_proxy in working_proxies.items(): print(p_name, p_proxy)