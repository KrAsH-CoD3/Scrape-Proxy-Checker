import asyncio, aiohttp, json
from bs4 import BeautifulSoup
from aiohttp_socks import ProxyConnector
from actions import getProxy, writeJson, selectedCountryProxies

apiRespList: list = getProxy()
writeJson(apiRespList)  # Write into APIProxy.json
proxies: dict = selectedCountryProxies()  # Write into proxy.json

async def test_proxy(proxy_name, proxy):
    connector = ProxyConnector.from_url(f'socks5://{proxy["Proxy"]}')
    async with aiohttp.ClientSession(connector=connector) as session:
        try:
            async with session.get('https://myip.link/mini/') as resp:
                response = await resp.text()
                soup1 = BeautifulSoup(response, "html.parser")
                api_resp = soup1.find('div', attrs={'class': 'request-info'})
                tz_time = json.loads(api_resp.text)["timezoneTime"]
                country_name = json.loads(api_resp.text)["countryName"]
                tz_name = json.loads(api_resp.text)["timezone"]["name"]
                is_tor = json.loads(api_resp.text)["security"]["isTor"]
                threat_score = json.loads(api_resp.text)["security"]["threatScore"]
            counter = 1
            is_proxy = "getFailed"  # Default value incase WHOER doesn't load up
            is_anonymizer = "getFailed"  # Default value incase WHOER doesn't load up
            while True:
                async with session.get('https://whoer.net/') as whoerResp:
                    try:
                        whoerResponse = await whoerResp.text()
                        soup2 = BeautifulSoup(whoerResponse, "html.parser")
                        is_proxy = soup2.find('span', class_='cont proxy-status-message').text.strip()
                        is_anonymizer = soup2.find('span', class_='value').text.strip()
                        if is_anonymizer in ["Yes", "No"]:
                            break
                        elif counter == 5:
                            break
                    except Exception: pass
                counter += 1
            if ((int(threat_score) <= 50) and (is_tor == False)):  # and \
                # (is_proxy == "No") and (is_anonymizer == "No")):
                print(f'{proxy["Proxy"]} => {country_name} {tz_name} has proxy: {is_proxy} and anonymizer: {is_anonymizer} with {threat_score} threat score')
        except Exception: pass

async def main():
    tasks = [test_proxy(proxy_name, proxy) for proxy_name, proxy in proxies.items()]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())