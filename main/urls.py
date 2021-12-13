from rest_framework.routers import DefaultRouter
from .viewsets import ShopViewSet, AddressViewSet
from django.urls import include, path

router = DefaultRouter()
router.register("shop", ShopViewSet, "shop")
router.register("address", AddressViewSet, "address")

urlpatterns = router.urls
