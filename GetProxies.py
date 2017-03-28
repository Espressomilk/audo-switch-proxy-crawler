import urllib.request
import urllib.parse
import re
import http.cookiejar

from bs4 import BeautifulSoup


def getHTML(url):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),
                         ('Cookie', '4564564564564564565646540')]
    urllib.request.install_opener(opener)
    html_bytes = urllib.request.urlopen(url).read()
    html_string = html_bytes.decode('utf-8')
    return html_string


def getProxyIps():
    indexURL = r'https://free-proxy-list.net/'

    html_doc = getHTML(indexURL)
    soup = BeautifulSoup(html_doc, 'html.parser')

    table = soup.find('table')
    tbody = table.find('tbody')
    tr_list = tbody.find_all('tr')
    results = []

    for tr in tr_list:
        td_list = tr.find_all('td')
        res = {}
        res['IP'] = td_list[0].string + ':' + td_list[1].string
        res['HTTPS'] = td_list[6].string
        results.append(res)

    return results
