import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

def getbili(name, limit=99):
        
    dic = {}
    url = 'http://search.bilibili.com/all?keyword=' + urllib.parse.quote(name) + '&from_source=nav_search&order=pubdate&duration=0&tids_1=13&tids_2=152'
    html = urllib.request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(html, "html.parser")
    info = soup.find_all('div',"info")
    for each in info:
        href = each.find_all('a')[0].get('href')
        link = 'https://' + re.findall('(www.+)\?.*', href)[0]
        title = each.find_all('a')[0].get('title').strip()
        description = each.find_all('div')[1].get_text().strip()
        uper = each.find_all('div')[2].contents[-1].get_text()
        if len(dic) < limit:
            all = title + description + 'UP主: ' + uper + '\n' + link
            dic[all] = []

    return dic

