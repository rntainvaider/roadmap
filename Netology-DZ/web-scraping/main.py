import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'Python', 'Илона', 'Как', 'Data']

url_site = "https://habr.com/ru/all/"

response = requests.get(url_site)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for article in soup.find_all('article'):
        date = article.find('time')
        title = article.find('h2')
        links = article.find('a', class_='tm-title__link')
        for keyword in KEYWORDS:
            if keyword in title.text:
                print(f"<{date.get('title')}> - <{title.text}> - <{'https://habr.com' + links.get('href')}>")
