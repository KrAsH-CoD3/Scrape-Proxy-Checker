from actions import *
from configparser import ConfigParser


cfg = ConfigParser(interpolation=None)
cfg.read('config.ini')


proxy_endpoint = "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_geolocation_anonymous/socks5.txt"

apiRespList: list = """47.100.182.178:443|Hong Kong|Central and Western District|Central
138.68.124.120:59166|Germany|Hesse|Frankfurt am Main
185.86.5.162:8975|Turkey|Istanbul|Istanbul
193.123.81.52:443|United States|California|San Jose
47.243.95.228:10080|Hong Kong|Central and Western District|Central
146.145.199.117:8080|United States|Pennsylvania|Bala-Cynwyd
188.34.140.205:1080|Germany|Saxony|Falkenstein
45.32.114.246:8081|Austria|Vienna|Vienna
103.111.225.93:1090|Bangladesh|Chittagong|Chittagong
185.87.121.35:8975|Turkey|Istanbul|Istanbul
125.141.139.55:5566|Germany|Brandenburg|Brandenburg
192.154.247.123:9000|United States|Florida|Orlando
45.132.75.19:36090|Brazil|Minas Gerais|Uberlândia
213.188.208.179:80|Japan|Tokyo|Tokyo
45.132.75.19:16863|Iraq|Baghdad|Baghdad""".split("\n")

if __name__ == "__main__":
    # apiRespList: list = getProxy(proxy_endpoint)
    # apiRespList: list = serverProxy.split("\n")
    writeJson(apiRespList)  # Write into APIProxy.json
    # print(selectedCountryProxies())  # Write into proxy.json

