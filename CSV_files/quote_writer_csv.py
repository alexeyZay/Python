import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("http://quotes.toscrape.com/")
html_data = BeautifulSoup(response.text, "html.parser")
quots_list = html_data.find_all(class_='quote')
with open('quote.csv', "w") as file:
    quote_writer = csv.writer(file)
    quote_writer.writerow(['text','Auther','Content'])
    for quote in quots_list:
        text = quote.find(class_='text').get_text()
        author = quote.find(class_='author').get_text()
        content = quote.find(class_='keywords')['content']
        quote_writer.writerow([text,author,content])