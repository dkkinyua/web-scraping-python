from bs4 import BeautifulSoup
import requests

with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

for article in soup.find_all('div', class_='header'):
    heading = article.h3.text
    print(heading)

    content = article.p.text
    print(content)

    print()

    