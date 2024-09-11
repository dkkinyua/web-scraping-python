import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

source = requests.get(os.getenv('WEBSITE_URL')).text

soup = BeautifulSoup(source, 'lxml')

heading = soup.find('h4').text

print(heading)

