import csv
import bs4
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import openpyxl
f=open('dataoutput.csv','a',newline='')
writer = csv.writer(f)
country=['USD','EUR','JPY','BGN','CZK','DKK','GBP','HUF','CHF','AUD','BRL','CAD','TRY','IDR','MYR','NZD']
currencies=[]
abbrs=[]
for i in range(0,len(country)):
    r=requests.get('https://www.iban.com/currency-converter?from_currency=INR&to_currency='+ str(country[i])+'&amount=1')
    soup=bs4.BeautifulSoup(r.text,"xml")
    currencies.append(soup.find_all('strong')[1].text)
    abbrs.append(soup.find_all('tr')[1].find_all('td')[2].text)
    localtime=time.asctime(time.localtime(time.time()))
    i=i+1



currency_rates=pd.DataFrame(
    {
      'Currency Name':abbrs,
       localtime:currencies,
    }
    )
writer.writerow(currency_rates)
for i in range(0,len(country)):

    writer.writerow(currencies[i])
    #writer.writerow(item.replace(",","") for item in currencies[i])
    i=i+1

print(currency_rates)