import urllib
from html.parser import HTMLParser
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests


class link_crawler(HTMLParser):
    reqt = ''
    soup = ''
    count=0
    def __init__(self, start_link, web_url):
        super().__init__()
        self.start_link = start_link
        self.web_url = web_url
        self.urls = set()


    def handle_starttag(self, tag, found_attributes):     # The main logic for crawler
        if tag == 'a':
            for (attr, value) in found_attributes:
                if attr == 'href':
                    url = urllib.parse.urljoin(self.start_link, value)

                    self.reqt = (requests.get(url))
                    self.soup = BeautifulSoup((self.reqt).text, "lxml")
                    category = self.soup.find_all("a", {"class":"a-link-normal a-color-tertiary"})
                    category = [(x.text).replace("\n","").replace(" ","") for x in category]
                    
                    l = ['Amazon Fashion', 'Amazon Global Store ', 'Amazon Pantry', 'Appliances', 'Baby', 'Beauty','Clothing & Accessories','Collectibles','Computers & Accessories','Gift Cards' ,'Health & Personal Care ','Jewellery','Kindle Store' ,'Luggage & Bags' ,'Luxury Beauty' ,'Office Products' ,'Shoes & Handbags' ,'Sports, Fitness & Outdoors' ,'Used & Refurbished' ,'Watches']
                    self.count = self.count + 1
                    print(self.count)
                    if category is None:
                        continue

                    else:
                        self.urls.add(url)
                        continue

    def page_urls(self):
        return self.urls

    def error(self, message):
        pass

# from urllib.request import urlopen

# received_response = urlopen('https://www.amazon.in/Fossil-Chronograph-Black-Dial-Watch/dp/B003R7JYFU/ref=br_asw_pdt-5?pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=6JH3J8V2V8Z7EKPP60EB&pf_rd_t=36701&pf_rd_p=5a1486c7-4fc3-4713-956f-3633eb9982d4&pf_rd_i=desktop')
# data_bytes = received_response.read()
# html_data_string = data_bytes.decode("latin-1")

# link_finder = link_crawler('https://www.amazon.in/', 'https://www.amazon.in/Fossil-Chronograph-Black-Dial-Watch/dp/B003R7JYFU/ref=br_asw_pdt-5?pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=6JH3J8V2V8Z7EKPP60EB&pf_rd_t=36701&pf_rd_p=5a1486c7-4fc3-4713-956f-3633eb9982d4&pf_rd_i=desktop')

# link_finder.feed(html_data_string)

# a = link_finder.page_urls()


# pprint(len(a))
# #"class":"a-link-normal a-color-tertiary"
# ['Amazon Fashion', 'Amazon Global Store ', 'Amazon Pantry', 'Appliances', 'Baby', 'Beauty','Clothing & Accessories','Collectibles','Computers & Accessories','Gift Cards' ,'Health & Personal Care ','Jewellery','Kindle Store' ,'Luggage & Bags' ,'Luxury Beauty' ,'Office Products' ,'Shoes & Handbags' ,'Sports, Fitness & Outdoors' ,'Used & Refurbished' ,'Watches']