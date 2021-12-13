from rest_framework.routers import DefaultRouter
from .model_viewsets import ShopViewSet, AddressViewSet

router = DefaultRouter()
router.register("shop", ShopViewSet, "shop")
router.register("address", AddressViewSet, "address")

urlpatterns = router.urls
