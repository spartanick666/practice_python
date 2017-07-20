#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles
# on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

headings = soup.find_all(class_="story-heading")

for i in headings:
    print(i.get_text().strip())


list = []

for i in headings:
    list.append(i.get_text().strip())

print("\nThe number of article titles on nytimes.com is: " , len(list))