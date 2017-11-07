import requests
from bs4 import BeautifulSoup

r = requests.get('http://pythonhow.com/example.html')
c = r.content

soup = BeautifulSoup(c, 'html.parser')
divs = soup.find_all('div', {'class': 'cities'})

cities = [div.find_all('h2')[0].text for div in divs]
print(cities)
