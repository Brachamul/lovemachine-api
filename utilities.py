from timeit import default_timer as timer
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed



def api_decorator(function):

	''' This decorator converts a python object into a JsonResponse that can
	be sent to the browser. It also measures the response_time of the call.'''

	def wrapper(*args, **kwargs):
		try :
			start = timer()
			output = function(*args, **kwargs)
			end = timer()
			response_time = round(end-start, 3)
			output['response_time'] = response_time
		except Exception:
			return function(*args, **kwargs)
		else:
			# If the output is already an HttpResponse, we use that as our final output
			# This will typically occur when the decorated function returns an HTTP 4xx message
			if issubclass(output.__class__, HttpResponse) :
				return output
			else :
				return JsonResponse(output, safe=False)

	return wrapper



def requires_method(function, method):

	''' A decorator that requires a given method, ie "POST" or "GET" '''

	def wrapper(*args, **kwargs):
		if not request.method == method:
			return HttpResponseNotAllowed([method,])
		else :
			return function(*args, **kwargs)

	return wrapper



def timeit(function):

	''' A decorator, @timeit, used to print the amount of time taken by a given function '''

	def timed(*args, **kwargs):

		start = timer()
		result = function(*args, **kwargs)
		end = timer()


		print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te-ts))
		return result

	return timed