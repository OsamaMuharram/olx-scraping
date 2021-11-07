import requests
from bs4 import BeautifulSoup
import pandas as pd
title=[]
description=[]
link=[]
ad_date=[]
price=[]
loop=1

url = 'https://www.olx.com.eg/properties/vacation-homes-for-sale/alexandria/'
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}
url_content = requests.get(url, headers=headers)
soup = BeautifulSoup(url_content.content, "html.parser")
pages = soup.find_all(attrs={"class": "block br3 brc8 large tdnone lheight24"})
print(pages[-1].text)


while(loop<int((pages[-1].text))):

   try:
      print('loop',loop)
      url=url+'?page={}'.format(loop)
      print(url)
      result= requests.get(url, headers = headers)
      print(result)
      soup = BeautifulSoup(result.content, "html.parser")
      pages= soup.find_all(attrs={"class":"block br3 brc8 large tdnone lheight24"})
      print(pages[-1].text)
      _class= soup.find_all(attrs={"class": "ads__item__ad--title"})

      loop=loop+1

      for i in _class :

         #price.append(price_list[_class.index(i)])

         ad = requests.get(i['href'], headers=headers)
         ad_soup = BeautifulSoup(ad.content, "html.parser")

         ad_price = ad_soup.find(attrs={"class": "pricelabel tcenter"}).contents[1].string
         ad_description= ad_soup.find(attrs={"id": "textContent"}).p.text
         _ad_date = ad_soup.find(attrs={"class": "pdingleft10 brlefte5"}).contents[0].text.replace("تم إضافة الإعلان", "")
         ad_date.append(" ".join(_ad_date.split()))
         description.append( " ".join(ad_description.split()) )
         price.append(ad_price)
         link.append(i['href'])
         title.append(" ".join((ad_soup.find('h1').string).split()))
         print(_class.index(i))
   except:
      print('fault')
      break
df = pd.DataFrame({'product_name':title , 'link':link , "price": price,' description':description ,' Date':ad_date })
export_csv = df.to_csv (r'C:/Users/osama/Desktop/Data.csv', index = None, header=True)

