# web1.py

from bs4 import BeautifulSoup

page = open("Chape09_test.html","rt",encoding="utf-8").read()

#

soup = BeautifulSoup(page,"html.parser")

#전체보기

print(soup.prettify())