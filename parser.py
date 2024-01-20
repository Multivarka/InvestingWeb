import requests
from bs4 import BeautifulSoup as bs
from url_list import dict_url
import lxml


def get_cat_info(session, category):
    URL = dict_url[category]
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0'}
    req = session.get(URL, headers=headers)
    result = []
    if req.status_code == 200:
        soup = bs(req.text, 'lxml')
        table = soup.find('table', {'class': 'W(100%)'})
        list_name = table.find_all('td', {'aria-label': 'Name'})
        list_price = table.find_all('td', {'aria-label': 'Last Price'})
        list_change = table.find_all('td', {'aria-label': 'Change'})
        if len(list_name) == len(list_price) == len(list_change):
            for i in range(len(list_name)):
                result += [[list_name[i].text, list_price[i].text, list_change[i].text]]
        return result

session = requests.Session()
for cat in dict_url:
    print(get_cat_info(session, cat))