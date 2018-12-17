from .models import App
from rest_framework import viewsets
from .serializers import AppSerializer
from play_store.calls import search
from django.shortcuts import render



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
    queryset = App.objects.all()
    serializer_class = AppSerializer
    lookup_field = "store_id"

def search_view(request):
    if request.POST :
        query = request.POST.get('query')
        search_results = search(query)
        context = {'query': query, 'search_results': search_results}
    else :
        context = {}
    return render(request, 'play_store/search.html', context=context) 
