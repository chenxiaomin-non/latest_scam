from ctypes import sizeof
import json
import requests
from bs4 import BeautifulSoup as bs4_

cookies = {
    'cf_clearance': '0UyDBKZPqdXkeh01yvNdQzqI1ddX5JjHTH3nNZODm2I-1662456331-0-150',
    '_gid': 'GA1.2.981642627.1662456331',
    '_ga': 'GA1.1.1260839281.1662456331',
    '_ga_L3ZW43PT32': 'GS1.1.1662456331.1.1.1662457541.0.0.0',
}

headers = {
    'authority': 'tokensniffer.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'cf_clearance=0UyDBKZPqdXkeh01yvNdQzqI1ddX5JjHTH3nNZODm2I-1662456331-0-150; _gid=GA1.2.981642627.1662456331; _ga=GA1.1.1260839281.1662456331; _ga_L3ZW43PT32=GS1.1.1662456331.1.1.1662457541.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
}

def get_latest_scam_token():
    url = 'https://tokensniffer.com/tokens/scam'
    r = requests.get(url, cookies=cookies, headers=headers).text
    soup = bs4_(r, 'html.parser')
    
    data = soup.find('script', {'id': '__NEXT_DATA__'}).text
    
    list_token = json.loads(data)['props']['pageProps']['tokens']
    return_list = []
    
    for token in list_token:
        new_return_token = {
            'index': len(return_list) + 1,
            'name': token['name'],
            'symbol': token['symbol'],
            'chain': token['network'],
            'address': token['addr'],
            'owner': token['from_addr'],
        }
        return_list.append(new_return_token)
        
    return return_list

from pprint import pprint
pprint(get_latest_scam_token())