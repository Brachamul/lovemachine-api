import requests
import datetime as dt
from bs4 import BeautifulSoup
from dataclasses import dataclass



@dataclass
class App(object):

	store_id: str
	name: str
	dev_id: str
	category: str=None
	subcategory: str=None
	short_description: str=None
	long_description: str=None
	thumbnail: str=None
	screenshots: str=None
	rating: int=None
	reviews: int=None
	installs: str=None
	maturity: str=None
	size: str=None
	is_free: bool=True
	display_price: str=None
	full_price: str=None
	has_ads: bool=None
	has_iaps: bool=None
	current_version: str=None
	android_version: str=None
	already_exists: bool=None
	date_last_updated: dt.date=None

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()



def search(query):

	url = "https://play.google.com/store/search?c=apps&q=" + query
	headers = {"Accept-Language": "en-US,en;q=0.5"}
	page = requests.get(url, headers=headers)
	soup = BeautifulSoup(page.content.decode(), 'lxml')
	scraped_apps = soup.select('div.card.apps')
	apps = []

	completed = 0
	for scraped_app in scraped_apps:
		completed += 1
		print('* #{}/{}, fetching data from app...'.format(completed,len(scraped_apps)), end="\r")
		app = App(
			store_id=scraped_app['data-docid'],
			name=scraped_app.find('a', class_='title')['title'].strip(),
			dev_id=scraped_app.find('a', class_='subtitle')['title'].strip(),
			)
		rating = scraped_app.find('div', class_="current-rating")
		app.category = "GAME"
		if rating: app.rating = int(float(rating['style'].replace('width: ', '').replace('%;', '')))
		app.short_description = scraped_app.find('div', class_='description').text.strip()
		app.thumbnail = scraped_app.find('img', class_="cover-image")['src']
		display_price = scraped_app.find('div', class_="display-price")
		full_price = scraped_app.find('div', class_="full-price")
		app.is_free != display_price
		if display_price: app.display_price = display_price.text
		if full_price: app.full_price = full_price.text
		apps.append(app)

	return apps