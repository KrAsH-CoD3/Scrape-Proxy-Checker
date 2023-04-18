import contextlib
import os
import requests, json

socks5 = True

def cleanJson(jsonName) -> None:
    # Clean everything in the json file (DELETE)
    with open(f"jsons/{jsonName}", "rb+") as j_file:
        fileee: str = j_file.read()
        file_length: int = len(fileee)
        j_file.seek(0, 2)
        j_file.seek(j_file.tell() - file_length)
        j_file.truncate()

def writeJson(responseList) -> None:
    cleanJson("APIProxy.json")

    # Write to JsonFile (Formatted Raw API)
    with open("jsons/APIProxy.json", "a+") as proxy_json:
        proxy_json.write("{\n")

        for idx, data in enumerate(responseList):
            proxy, country, region, city = data.split("|")
            proxyaddr: str = f'"Proxy {str(idx+1)}": ' + \
                '{"Proxy": ' + f'"{proxy}", "Country": ' + \
                f'"{country}", "Region": ' + \
                f'"{region}", "City": ' + f'"{city}"' + '}'
            try:
                proxy_json.write(proxyaddr + "\n}") if idx == len(
                    responseList)-1 else proxy_json.write(f"{proxyaddr},\n")
            except UnicodeEncodeError: 
                if idx == len(responseList)-1:
                    proxy_json.seek(proxy_json.tell() - 3)  # Move back two characters from the end of the file
                    proxy_json.truncate()
                    proxy_json.write("\n}")
            finally: proxy_json.flush()

def selectedCountryProxies() -> dict:
    # Get API proxy from json
    with open("jsons/APIProxy.json", "r") as jsonfile:
        read_file: str = jsonfile.read()

    return json.loads(read_file)
    # proxyAddrs: json = json.loads(read_file)
    # selected_Proxies: dict = {}
    # selected_countries: list = ["Canada", "France", "Ukraine", "United Kingdom", "Germany", \
    #     "Australia", "United States"]

    # for (key, value) in proxyAddrs.items():
    #     # country: str = value.get("Country",  "Key: 'Country' not found")
    #     # if country in selected_countries:
    #     selected_Proxies[key] = value

    # cleanJson("proxy")

    # # Write to proxy (Selected Country Proxies)
    # with open("proxy.json", "a+") as p:
    #     json.dump(selected_Proxies, p, indent=4)  # For reference purpose
    # return selected_Proxies  # This is what we need
    # return proxyAddrs  # This is what we need

def get_proxy():
    if socks5:
        pass

