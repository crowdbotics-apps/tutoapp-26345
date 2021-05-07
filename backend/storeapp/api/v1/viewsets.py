from rest_framework import authentication
from storeapp.models import Products
from .serializers import ProductsSerializer
from rest_framework import viewsets


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Products.objects.all()
