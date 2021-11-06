import requests
from bs4 import BeautifulSoup
import pandas as pd
serial=[]
title=[]
description=[]
link=[]
ad_date=[]
price=[]
loop=1
while(1):

   try:
      url='https://www.olx.com.eg/jobs/hr-recruiting/?search%5Bfilter_enum_field%5D%5B0%5D=1&search%5Bfilter_enum_field%5D%5B1%5D=5&search%5Bfilter_enum_field%5D%5B2%5D=4&page={}'.format(loop)
      print(url)
      headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
      }
      result= requests.get(url, headers = headers)
      print(result)
      soup = BeautifulSoup(result.content, "html.parser")
      _class= soup.find_all(attrs={"class": "ads__item__ad--title"})


      for i in _class :

         #price.append(price_list[_class.index(i)])
         ad = requests.get(i['href'], headers=headers)
         ad_soup = BeautifulSoup(ad.content, "html.parser")
         try:
            ad_price = ad_soup.find(attrs={"class": "pricelabel tcenter"}).contents[1].string
         except:
            pass
         ad_description= ad_soup.find(attrs={"id": "textContent"}).p.text
         _ad_date = ad_soup.find(attrs={"class": "pdingleft10 brlefte5"}).contents[0].text.replace("تم إضافة الإعلان", "")
         serial.append(_class.index(i))
         ad_date.append(" ".join(_ad_date.split()))
         description.append( " ".join(ad_description.split()) )
         price.append(ad_price)
         link.append(i['href'])
         title.append(" ".join((ad_soup.find('h1').string).split()))
         loop = loop + 1
         print('done')
   except:
      print('fault')
      break
df = pd.DataFrame({'serial':serial ,'product_name':title , 'link':link ,'price':price  ,' description':description ,' Date':ad_date })
export_csv = df.to_csv (r'C:/Users/osama/Desktop/Data.csv', index = None, header=True)

