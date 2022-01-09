import requests as r
from bs4 import BeautifulSoup as bs

import UserAgents as ua
import random

def createUserAgents():
    return f"User-Agent : ${ua.UserAgents[random.randint(0,len(ua.UserAgents)-1)]}"
    
def createRiskyUserAgents():
    return f"User-Agent : ${ua.RiskyUserAgents[random.randint(0,len(ua.RiskyUserAgents)-1)]}"

def createProxy(proxies):
    proxies = proxies.get('data')
    proxy = proxies[random.randint(0,len(proxies)-1)]
    proxies = {
   'http': f"http://{proxy.get('ip')}:{proxy.get('port')}",
   'https': f"https://{proxy.get('ip')}:{proxy.get('port')}",
}
# you can replace the f strings with your proxy that works  
    print(proxies)
    return proxies

def createProxyDic():
    proxylist = get("https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&filterUpTime=100&speed=fast&protocols=https")
    if proxylist.status_code == 200:
        proxies = proxylist.json()
        return createProxy(proxies) 
    else:
        print ("Proxylist down")
    #FREE PROXIES ARE KINDA BROKEN'- most likely won't work. U can use https://openproxy.space/ or https://spys.one/en/ or some better side. it sometimes work:D


def get(url):
    headers = createUserAgents()
    page = r.get(url,headers)
    return page

def proxyGet(url):
    proxies = createProxyDic()
    page = r.get(url,proxies=proxies)
    return page

def soup(page):
    return bs(page.content, 'html.parser')

def Main():
    """
Parse your things here from the soup object - suggest using things like find_all("a", class_="sister") / you can also use list ("a", ["stylelistrowone", "stylelistrow"])
expected usage is soup(get("https://example.com")) and then anything you love.

Scrape the world! 
"""
