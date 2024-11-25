import bs4
import requests
import selenium

url = "https://ria.ru/"
site_date = requests.get(url)
html = site_date.text
soup = bs4.BeautifulSoup(html)
