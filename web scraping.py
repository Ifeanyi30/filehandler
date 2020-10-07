import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

rep = http.request('GET','https://www.facebook.com')

soup = BeautifulSoup(rep.data, "html.parser")

# my way of getting the link tags

with open('c:/Users/Ifeanyi Eze/Documents/facebook.html', 'a', encoding='utf-8') as facebook:

    facebook.write(soup.prettify())

links = soup.find_all('a')

print(links)