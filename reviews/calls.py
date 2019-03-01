from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST

from utilities import api_decorator

from android_apps.models import AndroidApp
from django.http import HttpResponseBadRequest
from django.forms.models import model_to_dict

from android_users.models import AndroidUser
from .models import AndroidAppReview


@api_decorator
def store_app():
	pass



@api_decorator
def get_rated_games():
	pass



@api_decorator
def get_recommendations(user_name):
	pass



@api_decorator
@require_GET
def rate(request):
	# Getting params from URL
	google_gamer_id = request.GET.get('google_gamer_id', False)
	google_app_id = request.GET.get('google_app_id', False)
	rating = int(request.GET.get('rating', False))
	# Fetching database resources
	android_user = get_object_or_404(AndroidUser, google_gamer_id=google_gamer_id)
	android_app = get_object_or_404(AndroidApp, google_app_id=google_app_id)
	# Verifying data integrity
	if rating not in [0, 34, 66, 100]:
		return HttpResponseBadRequest('400 Bad Request - Parameter "rating" must have a value of 0, 34, 66 or 100, not {}.'.format(rating))
	# Creating review
	review, created = AndroidAppReview.objects.get_or_create(
		android_user=android_user,
		android_app=android_app,
		rating=rating
		)
	return {'review': {'id': review.id, 'android_user': google_gamer_id, 'android_app': google_app_id, 'rating': rating},}