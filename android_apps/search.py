import requests
from bs4 import BeautifulSoup
from .models import AndroidApp

from timeit import default_timer as timer

def search_play_store(query):

	''' When called, returns a list of games it could find based on that name '''

	url = "https://play.google.com/store/search?c=apps&q=" + query
	headers = {"Accept-Language": "en-US,en;q=0.5"}
	page = requests.get(url, headers=headers)
	soup = BeautifulSoup(page.content.decode(), 'lxml')
	scraped_apps = soup.select('div.card.apps')
	dict_of_apps = {}

	for scraped_app in scraped_apps:

		app_data = {}
		app_data['google_app_id'] = scraped_app['data-docid']
		app_data['category'] = "GAME"
		app_data['name'] = scraped_app.find('a', class_='title')['title'].strip()
		app_data['dev_id'] = scraped_app.find('a', class_='subtitle')['title'].strip()
		
		rating = scraped_app.find('div', class_="current-rating")
		if rating: app_data['rating'] = int(float(rating['style'].replace('width: ', '').replace('%;', '')))

		app_data['short_description'] = scraped_app.find('div', class_='description').text.strip()
		app_data['thumbnail'] = scraped_app.find('img', class_="cover-image")['src']

		display_price = scraped_app.find('span', class_="display-price")
		if display_price == '<span class="display-price"></span>' or display_price == None:
			app_data['display_price'] = None
			app_data['is_free'] = True
		else:
			app_data['display_price'] = display_price.text
			app_data['is_free'] = False

		full_price = scraped_app.find('div', class_="full-price")
		if full_price: app_data['full_price'] = full_price.text

		google_app_id = app_data['google_app_id']
		dict_of_apps[google_app_id] = app_data

	found_google_app_ids = dict_of_apps.keys()

	apps_already_in_database = AndroidApp.objects.filter(google_app_id__in=found_google_app_ids)
	existing_google_app_ids = [app.google_app_id for app in apps_already_in_database]
	new_google_app_ids = set(found_google_app_ids).difference(set(existing_google_app_ids))

	new_apps = [AndroidApp(**dict_of_apps[google_app_id]) for google_app_id in new_google_app_ids]

	AndroidApp.objects.bulk_create(new_apps)

	return dict_of_apps
