from .models import App
from rest_framework import viewsets
from .serializers import AppSerializer



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