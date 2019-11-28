# Python program to scrape website
# and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content,'html5lib')
quotes = []  # a list to store quotes
table = soup.findAll('div', attrs={'class': 'container'})
containers=table[1]  # All quotes in container
All_quotes=containers.findAll('div',{'id':'all_quotes'})
Quote_2_list=All_quotes[0].findAll('div', attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'})
# print(len(Quote_2_list))

filename = 'inspirational_quotes2.csv'
f=open(filename,"w")
headers="link, source, text \n"
f.write(headers)

for row in Quote_2_list:
     quote = {}
     # print(row)
     # quote['theme'] = row.h5.text
     quote['url'] = row.a['href']
     quote['img'] = row.img['src']
     quote['text']= ''.join(row.img['alt'].split('#')[:-1])
     f.write(quote['url']+","+ quote['img'].replace(",","|")+","+quote['text']+'\n')