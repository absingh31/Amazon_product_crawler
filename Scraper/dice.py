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
	
		if im is None:
			return None

		im=re.findall(r'\bhttps\S*', im.replace('"',' '))	# making a list of images
	
		imgs = [i for i in im if(i.endswith('L.jpg'))]  # getting one image of all types

		if imgs:
			return list(set(imgs)) 	# returns list of images
		return None


	def meta_data(self):
		data = self.soup.find("div",{"id":"feature-bullets"})		# getting product description

		if data is None:
			return None

		data=str(data)
		data = data.replace('\t','')
		data = data.split('\n')
		data = [i for i in data if(not (i.startswith('<')))]		# removing noise
		data = list(filter(None, data))			# removing NULL values from 'data'
		
		if data: 
			return data

		return None


	def get_asin(self):
		asin=self.soup.find(text=re.compile('\\mediaAsin\\b'))	

		if asin is None:
			return None
		asin = (asin[-34:-24]).split("\\hehehaharandom")    # cuz asin number are 10 digit
		
		if asin:
			return asin
 
		return None


	def get_category(self):
		category = self.soup.find_all("a", {"class":"a-link-normal a-color-tertiary"})

		if category is None:
			return None   # returns categories as list

		category = [(x.text).replace("\n","").replace(" ","") for x in category]

		if category:
			return category

		return None


	def get_title(self):
		title = self.soup.find_all("span", {"class":"a-size-large"})

		if title is None:
			return None

		title = [(x.text).replace("\n","").replace(" ","") for x in title]

		if title:
			return title     # returns title in list

		return None

	def __del__(self):
		# just a deconstructor
		return 0



# Example use of the above defined class

prod = ProductData(input('Enter the url'))

from pprint import pprint

pprint(prod.get_asin())
pprint(prod.get_title())
pprint(prod.get_images())
pprint(prod.meta_data())
pprint(prod.get_category())
