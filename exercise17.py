#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles
# on the New York Times homepage.

import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(r_html, 'html.parser')

heading3 = soup.find_all(['h1'])
print(soup.find("h3",attrs={"class":"story-heading"}))

