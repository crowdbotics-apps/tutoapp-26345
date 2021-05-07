from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ProductsViewSet

router = DefaultRouter()
router.register("products", ProductsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
