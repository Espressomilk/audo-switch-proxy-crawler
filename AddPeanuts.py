import http.cookiejar
import urllib
from urllib.error import URLError, HTTPError

from GetProxies import getProxyIps

url = r'http://1point3acres.com/bbs/?fromuid=201556'

if __name__ == "__main__":
    proxy_ips = getProxyIps()
    success_time = 0
    for proxy_ip in proxy_ips:
        if(success_time > 8):
            break
        headers = [
            # ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
            # ("Accept-Encoding", "gzip, deflate"),
            # ("Accept-Language", "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3"),
            ("Connection", "keep-alive"),
            # ("Content-Length", "31"),
            ("Content-Type", "application/x-www-form-urlencoded"),
            ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36")]
        mode = 'http'
        if(proxy_ip['HTTPS'] == 'yes'):
            mode = 'https'
        proxy_handler = urllib.request.ProxyHandler({mode: proxy_ip['IP']})
        proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
        # proxy_auth_handler.add_password('realm', '123.123.2123.123', 'user', 'password')

        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), proxy_handler)
        opener.addheaders = headers
        urllib.request.install_opener(opener)

        # req = urllib.request.Request(url)
        # resp = urllib.request.urlopen(req)
        # print(1)

        try:
            req = urllib.request.Request(url)
            resp = urllib.request.urlopen(req)
        except URLError as e:
            print(proxy_ip['IP'] + ': failed')
        except Exception as e2:
            print(proxy_ip['IP'] + ': failed')
        else:
            success_time += 1
        print(proxy_ip['IP'] + ': Suceeded')
