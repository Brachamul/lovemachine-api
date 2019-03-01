from django.core.management.base import BaseCommand

from timeit import default_timer as timer

from android_apps.search import search_play_store
from android_apps.models import AndroidApp


class Command(BaseCommand):

	def handle(self, *args, **options):

		AndroidApp.objects.all().delete()
	
		queries = [
			'pokemon',
			'kingdom',
			'potato',
			'battle',
			'candy',
			'arena',
			'poney',
			'idle',
			'tap',
			'io',
		]

		times = []

		print("Searching...")
		for query in queries :
			start = timer()
			search_play_store(query)
			end = timer()
			time = round(end-start, 3)
			print('query "{}" completed in {} s'.format(query, time))
			times.append(time)

		average_time = round(sum(times) / len(times), 3)

		print("================================")
		print("Average time : {} s".format(average_time))

