import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

quotes = soup.find_all("div", class_="quote")

for i in range(len(quotes)):
    print(f"Цитата №{i+1}:")
    print(quotes[i].find("span", class_="text").text)
    print(f"Автор: {quotes[i].find("small", class_="author").text}\n")
