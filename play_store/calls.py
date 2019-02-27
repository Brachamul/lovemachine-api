import requests
import datetime as dt
from bs4 import BeautifulSoup
from .models import AndroidApp
from django.forms.models import model_to_dict



def search(query):

	''' When called, returns a list of games it could find based on that name '''

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
		app = AndroidApp(
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

		app = model_to_dict(app) # converting Model to Dict
		apps.append(app)

	return apps