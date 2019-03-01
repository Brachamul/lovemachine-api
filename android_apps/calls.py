from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from utilities import api_decorator
from .search import search_play_store



@api_decorator
@require_GET
def find(request):
	query = request.GET.get('query', False)
	if query:
		search_results = search_play_store(query)
		return {'apps': search_results, 'query': query, }
	else:
		return HttpResponseBadRequest('400 Bad Request - A "query" parameter is required.')