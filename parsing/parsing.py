import requests
from bs4 import BeautifulSoup
# from tickets.models import Ticket
headers = {'UserAgent': '/home/kurmanjan/Desktop/py.22/parsing_project/my_venv/bin/activate'}
url = f'https://avia.tutu.ru/aviabilety/kirgizstan/bishkek_152/'
response = requests.get(url, headers=headers)


def get_link(html):
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('div', class_="o33501 o33500 o3337 o33859")
    for i in data:
        f = i.find('a', class_="o33642 o33643 o33846 o33770 o33803").text.replace('\n', '').split('\xa0—')[0]
        t = i.find('a', class_="o33642 o33643 o33846 o33770 o33803").text.replace('\n', '').split('\xa0—')[1]
        p = i.find('span', class_="o33864 o33846 o33770 o33803").text

    return(f'{f}\n{t}\n{p}\n')


a = get_link(f'https://avia.tutu.ru/aviabilety/kirgizstan/bishkek_152/')



