import re

from bs4 import BeautifulSoup
import requests

site = ['https://moiraion.moscow/list/855',
        'https://moiraion.moscow/list/1449',
        'https://moiraion.moscow/list/855',
        'https://moiraion.moscow/list/552',
        'https://moiraion.moscow/list/1637',
        'https://moiraion.moscow/list/855',
        'https://moiraion.moscow/list/1114',
        'https://moiraion.moscow/list/887',
        'https://moiraion.moscow/list/1373',
        'https://moiraion.moscow/control/view/1272',
        'https://moiraion.moscow/list/755',
        'https://moiraion.moscow/list/348',
        'https://moiraion.moscow/list/861',
        'https://moiraion.moscow/list/1692',
        'https://moiraion.moscow/list/4159',
        'https://moiraion.moscow/list/1984',
        'https://moiraion.moscow/list/1249',
        'https://moiraion.moscow/list/4045',
        'https://moiraion.moscow/list/580',
        'https://moiraion.moscow/list/619']


def start():
    request = input('Введите запрос: ')
    for count,i in enumerate(site):
        url = i
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        request_site = soup.find('p', text=re.compile(request))
        try:
            print(f'Сайт: {count+1}\n Найдено: {request_site.text}')
        except:
            print('Не найдено')
    a = input('Продолжить? | y/n  ')
    if a == 'y':
        start()



if __name__ == "__main__":
    start()


