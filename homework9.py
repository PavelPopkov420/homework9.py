import requests
from bs4 import BeautifulSoup as bs

url = 'https://prostopogoda.ru/rus/bryanskaya_oblast/novozybkov/fevral-2023/'
response = requests.get(url).text
soup = bs(response, 'html.parser')

weather = soup.find('div', class_='post-head')
city = soup.find('h1', class_="title")

print(city.text)
print(weather.text)