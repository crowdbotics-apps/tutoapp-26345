from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ProductViewSet, ProductsViewSet

router = DefaultRouter()
router.register("products", ProductsViewSet)
router.register("product", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
