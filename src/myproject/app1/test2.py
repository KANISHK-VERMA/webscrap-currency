import requests
import bs4
from bs4 import BeautifulSoup
import openpyxl

abbrs = []
url = "https://www.gkquestionbank.com/list-of-different-currency-in-the-world/"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, "xml")
countries = soup.find_all("strong", {"class":""})
for country in range(3, (len(countries)-20), 2):
  abbrs.append(countries[country].text)
abbrs.remove('INR')
abbrs.remove('LTL')
abbrs.remove('VEF')
#print(abbrs)
for ar in abbrs:
  url2 = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=INR&To="+ar
  a=requests.get(url2)
  b=a.text
  soup2=bs4.BeautifulSoup(b,'html.parser')
  c=soup2.find_all('div',{'class_':'converterresult-conversionTo'}).find_all('span')[1]
  print(ar)
  print(c)