from actions import *
from scrape_proxy import scrape
from configparser import ConfigParser


cfg = ConfigParser(interpolation=None)
cfg.read('config.ini')


proxy_endpoint = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http"
# proxy_endpoint = "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_geolocation_anonymous/socks5.txt"


apiRespList: list = """185.161.210.184:21687|Netherlands|Flevoland|Dronten
190.2.136.37:57594|United States|Virginia|Boydton
47.243.95.228:10080|Hong Kong|Central and Western District|Central
115.205.2.114:1080|Hong Kong|Wan Chai|Wanchai
103.68.182.92:8009|Hong Kong|Kwai Tsing|Ha Kwai Chung
103.152.104.250:1080|Bangladesh|Dhaka Division|Dhaka
109.236.91.27:38247|United States|Oregon|Portland""".split("\n")

if __name__ == "__main__":
    # apiRespList: list = getProxy(proxy_endpoint)
    # apiRespList: list = serverProxy.split("\n")
        # writeJson(apiRespList)  # Write into APIProxy.json
    # print(selectedCountryProxies())  # Write into proxy.json

    proxy_list: list = scrape(proxy_endpoint)
    with open("Download.txt", "a+") as f:
        for idx, prox in enumerate(proxy_list):
            if prox == "": continue
            f.write(f"{prox.strip()}\n")
            f.flush()


