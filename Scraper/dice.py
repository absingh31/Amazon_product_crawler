import re
import requests
from pprint import pprint
from bs4 import BeautifulSoup


class ProductData:
	soup=''
	reqt=''
	def __init__(self, url):
		self.reqt = (requests.get(url))
		self.soup=BeautifulSoup((self.reqt).text,"lxml")			# making soup


	def get_images(self):	
		im=self.soup.find(text=re.compile('\\colorImages\\b'))		# finding product images
	
		im=re.findall(r'\bhttps\S*', im.replace('"',' '))	# making a list of images
	
		imgs = [i for i in im if(i.endswith('L.jpg'))]  # getting one image of all types

		if imgs:
			return list(set(imgs)) 	# returns list of images
		return None


	def meta_data(self):
		data = self.soup.find("div",{"id":"feature-bullets"})		# getting product description

		data=str(data)
		data = data.replace('\t','')
		data = data.split('\n')
		data = [i for i in data if(not (i.startswith('<')))]		# removing noise
		data = list(filter(None, data))			# removing NULL values from 'data'
		
		if data:
			return data 	# returns data in list format

		return None


	def get_asin(self):
		asin=self.soup.find(text=re.compile('\\mediaAsin\\b'))	

		if asin is None:
			get_asin()
		asin = (asin[-34:-24]).split("\\hehehaharandom")    # cuz asin number are 10 digit
		
		if asin is None:
			return None  # asin given as list

		return asin


	def get_category(self):
		category = self.soup.find_all("a", {"class":"a-link-normal a-color-tertiary"})

		category = [(x.text).replace("\n","").replace(" ","") for x in category]

		if category:
			return category   # returns categories as list
		else:
			return None


	def get_title(self):
		title = self.soup.find_all("span", {"class":"a-size-large"})

		title = [(x.text).replace("\n","").replace(" ","") for x in title]

		if title:
			return title
		else:
			return None     # returns title in list

	def __del__(self):
		# just to delete the object
		return 0



# Example use of the above defined class

prod = ProductData(input('Enter the url'))

from pprint import pprint

pprint(prod.get_asin())
pprint(prod.get_title())
pprint(prod.get_images())
pprint(prod.meta_data())
pprint(prod.get_category())
