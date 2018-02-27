from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import re
from pprint import pprint
import time
class ProductData:
    soup = ''
    reqt = ''

    def __init__(self, url):
        self.reqt = (requests.get(url))
        self.soup = BeautifulSoup((self.reqt).text, "lxml")  # making soup

    def get_images(self):
        im = self.soup.find(text=re.compile('\\colorImages\\b'))  # finding product images

        if im is None:
            return None

        im = re.findall(r'\bhttps\S*', im.replace('"', ' '))  # making a list of images

        imgs = [i for i in im if (i.endswith('L.jpg'))]  # getting one image of all types

        if imgs:
            return list(set(imgs))  # returns list of images
        return None

    def meta_data(self):
        data = self.soup.find("div", {"id": "feature-bullets"})  # getting product description

        if data is None:
            return None

        data = str(data)
        data = data.replace('\t', '')
        data = data.split('\n')
        data = [i for i in data if (not (i.startswith('<')))]  # removing noise
        data = list(filter(None, data))  # removing NULL values from 'data'

        if data:
            return data

        return None

    def get_asin(self):
        asin = self.soup.find(text=re.compile('\\mediaAsin\\b'))

        if asin is None:
            return None
        asin = (asin[-34:-24]).split("\\hehehaharandom")  # cuz asin number are 10 digit

        if asin:
            return asin

        return None

    def get_category(self):
        category = self.soup.find_all("a", {"class": "a-link-normal a-color-tertiary"})

        if category is None:
            return None  # returns categories as list

        category = [(x.text).replace("\n", "").replace(" ", "") for x in category]

        if category:
            return category

        return None

    def get_title(self):
        title = self.soup.find_all("span", {"class": "a-size-large"})

        if title is None:
            return None

        title = [(x.text).replace("\n", "").replace("  ", "") for x in title]

        if title:
            return title[0]  # returns title in list

        return None

    def __del__(self):
        # just a deconstructor
        return 0
# Example use of the above defined class
# prod = ProductData(input('Enter the url'))
url='https://www.amazon.in/'
driver=webdriver.Chrome()
driver.get(url)
category=driver.find_element_by_xpath('//*[@id="nav-link-shopall"]').click()
# driver.execute_script('arguments[0].click();',category)
time.sleep(0.2)
mens_fashion=driver.find_element_by_xpath('//*[@id="shopAllLinks"]/tbody/tr/td[2]/div[2]/ul/li[2]/a').click()
find_sponsor=driver.find_elements_by_css_selector('.a-spacing-none.a-color-tertiary.s-sponsored-header.sp-pixel-data.a-text-normal')
print(len(find_sponsor))
# driver.execute_script('arguments[0].click();',mens_fashion)
all_products=driver.find_elements_by_css_selector('.a-link-normal.s-access-detail-page.s-color-twister-title-link.a-text-normal')
print(len(all_products))
xpath='//*[@id="result_i"]/div/div[3]/div[1]/a'
new_xpath=xpath.split('_i')
for i in range(len(find_sponsor),20):
    abc=new_xpath[0] + '_' + str(i) + new_xpath[1]
    link=driver.find_element_by_xpath(abc).get_attribute('href')
    print(link)
    prod=ProductData(link)
    lund=prod.get_asin()
    while(lund==None):
        pr=ProductData(link)
        pprint(prod.get_asin())
        pprint(prod.get_title())
        pprint(prod.get_images())
        pprint(prod.meta_data())
        pprint(prod.get_category())
        print('\n')
        # time.sleep(5)
    pprint(prod.get_asin())
    pprint(prod.get_title())
    pprint(prod.get_images())
    pprint(prod.meta_data())
    pprint(prod.get_category())
    print('\n')
    # time.sleep(5)

# //*[@id="result_3"]/div/div[3]/div[1]/a
# //*[@id="result_4"]/div/div[3]/div[1]/a
# //*[@id="result_16"]/div/div[3]/div[1]/a
# //*[@id="result_37"]/div/div[3]/div[1]/a
# //*[@id="result_99"]/div/div[3]/div[1]/a
