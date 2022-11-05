import requests
from bs4 import BeautifulSoup
 
# Making a GET request
r = requests.get('https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch')
 
soup = BeautifulSoup(r.content, 'html.parser')
 
# Getting the title tag
print(soup.title)
print(soup.prettify())
 
# Getting the name of the tag
print(soup.title.name)
 
# Getting the name of parent tag
print(soup.title.parent.name)
 