from django.forms.models import model_to_dict
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods, require_GET, require_POST

from utilities import api_decorator

from .models import AndroidUser



@require_GET
@api_decorator
def get_or_create(request):
	google_gamer_id = request.GET.get('google_gamer_id', False)
	if not google_gamer_id :
		return HttpResponseBadRequest('400 Bad Request - A "google_gamer_id" parameter is required.')
	else :
		user, created = AndroidUser.objects.get_or_create(google_gamer_id=google_gamer_id)
		user = model_to_dict(user)
		del user['id']
		return {'user': user, 'created': created}