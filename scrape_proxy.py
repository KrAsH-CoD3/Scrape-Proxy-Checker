import contextlib
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

holding_proxies: list = []
end_points: list = [
    "https://spys.me/proxy.txt",
    "https://proxyspace.pro/http.txt",  
    "https://proxyspace.pro/https.txt",
    "https://openproxylist.xyz/http.txt",
    "https://rootjazz.com/proxies/proxies.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt",
    "https://raw.githubusercontent.com/ObcbO/getproxy/master/http.txt",
    "https://raw.githubusercontent.com/ObcbO/getproxy/master/https.txt",
    "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
    "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/rx443/proxy-list/main/online/http.txt",
    "https://raw.githubusercontent.com/rx443/proxy-list/main/online/https.txt",
    "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
    "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
    "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
]

# end_points = ["https://raw.githubusercontent.com/ObcbO/getproxy/master/https.txt",]

def scrape(endpoint) -> any :
    response = requests.get(fr"{endpoint}")
    # response = requests.get(r"https://proxyscan.io/download?type=http")
    # soup = BeautifulSoup(response.text, "html.parser")
    proxies: list = response.text.split("\n")  # REGULAR SCRAPING
    # proxies = pd.read_html(response.text)[0]["Ip:Port"]  # proxysearcher
    # proxies = pd.read_html(response.text)[0]["Proxy"]  # proxylist.live
    
    regex_pattern1 = r'^(.*?:){2}.*$'  # Contains two ':'
    regex_pattern2 = r'\s[a-zA-Z]{2}'  # Contain white space and any two alphabet
    regex_pattern3 = r'^(http|https|socks(4|5)?)://.*$'  # Has (http|https|socks|socks4|socks5)://
    regex_pattern4 = '^[^:]*$'  # Not containing colon

    with open("Download.txt", "a+") as f:
        for proxx in proxies:
            ip: str = proxx.split(":")[0]
            with contextlib.suppress(ValueError):
                if proxx == '': continue
                elif all([int(ip[0]) in range(1, 10), "\r" in proxx]):
                    if len(re.findall(r"\.", proxx)) == 3:
                        f.write(proxx.strip() + "\n")
                        f.flush()
                    elif len(re.findall(r"\.", proxx)) > 3:
                        proxx_list = proxx.split("\r")
                        for prox in proxx_list:
                            if prox == "": continue
                            f.write(prox + "\n")
                            f.flush()
                elif re.search(regex_pattern1, proxx):
                    second_ip_num_start: int = int(proxx.split(':')[1].split('.')[0][-3:])
                    if second_ip_num_start > 255:
                        second_ip_num_start: str = str(second_ip_num_start)[1:]
                    rem_2nd_ip_part = proxx.split(':')[1].split(f"{second_ip_num_start}.")
                    second_ip_port: str = proxx.split(':')[2]
                    ip2: str = (f"{second_ip_num_start}." + rem_2nd_ip_part[1] + ':' + second_ip_port).strip()
                    ip1: str = proxx.split(ip2)[0].strip()
                    if re.search(regex_pattern4, ip1): 
                        ip1 = ip1 + ':8080'  # Add default port if missing
                    if re.search(regex_pattern4, ip2): 
                        ip2 = ip2 + ':8080'  # Add default port if missing
                    proxx = f"{ip1}\n{ip2}"
                elif re.search(regex_pattern2, proxx): proxx = proxx.split(' ')[0]
                elif re.search(regex_pattern3, proxx): proxx = proxx.split('://')[1]
                # holding_proxies.append(f"{proxx.strip()}\n")
                
                if isinstance(int(proxx[0]), int):
                    f.write(f"{proxx.strip()}\n")
                    f.flush()

def graphical_scrape():
    options=Options()
    options.add_argument("--headless")
    options.add_experimental_option(
        "excludeSwitches", ["enable-automation", 'enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://openproxy.space/list/socks5")
    proxies_area = BeautifulSoup(driver.page_source, "html.parser")
    proxies = proxies_area.textarea.text.split("\n")
    driver.quit()

    for prox in proxies:
        if prox == "": continue
        holding_proxies.append(f"{prox.strip()}\n")
    
    with open("Download.txt", "a+") as f:
        for prox in proxies:
            if prox == "": continue
            f.write(f"{prox.strip()}\n")
            f.flush()

if __name__ == "__main__":
    [scrape(i) for i in end_points]
    # graphical_scrape()
    # print(len(holding_proxies))