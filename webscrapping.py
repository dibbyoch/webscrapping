from bs4 import BeautifulSoup

import requests

get_url ="https://www.goibibo.com/hotels/hotels-in-delhi-ct/"

page = requests.get(get_url)

soup = BeautifulSoup(page.content, 'html.parser')
hold1 = [];hold2 = []
lists = soup.find_all('section', class_ = "HotelCardstyles__PricingCompleteSection-sc-1s80tyk-57 iYqpNR")

for liste in lists:
  dis_price = liste.find('p', class_ = "HotelCardstyles__CurrentPrice-sc-1s80tyk-31 hBNuAQ").text
   
  hold1.append(dis_price)

mlists = soup.find_all('div', class_ = "HotelCardstyles__WrapperSectionMetaDiv-sc-1s80tyk-5 jjHNnh")

for lister in mlists:
  hotel_name = lister.find('a',class_ = "HotelCardstyles__HotelNameSeoAnchor-sc-1s80tyk-16 eUMfTF").text
  hold2.append(hotel_name)

for i in range(len(hold1)):
  print([hold1[i],hold2[i]])

