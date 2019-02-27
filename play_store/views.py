from .models import AndroidApp
from rest_framework import viewsets
from .serializers import AppSerializer
from play_store.calls import search
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest



class CreateListModelMixin (object):

    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)



class AppViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows Apps to be read, added or updated
    """
    queryset = AndroidApp.objects.all()
    serializer_class = AppSerializer
    lookup_field = "store_id"



def search_view(request):
    return render(request, 'play_store/search.html')



def search_api(request):
    query = request.GET.get('query')
    search_results = search(query)
    return JsonResponse({'apps': search_results})