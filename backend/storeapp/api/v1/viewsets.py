from rest_framework import authentication
from storeapp.models import Product, Products
from .serializers import ProductSerializer, ProductsSerializer
from rest_framework import viewsets


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Products.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Product.objects.all()
