from rest_framework.routers import DefaultRouter

from .model_viewsets import (
    ShopViewSet as ShopModelViewSet,
    AddressViewSet as AddressModelViewSet
)
from .viewsets import ShopViewSet, AddressViewSet
"""
model_viewsets contains viewsets of ModelViewSets.
These ones I created when I was doing the first version of app.
I think they should be in final version of app because they provide extra functionality
model_viewsets are located in URLs /model_shop/ and /model_address/

Completed task is located by the following URLs:

GET /shop/
GET /address/{id}/shops/
GET /shop/{id}/
POST /address/
POST /shop/
PATCH /shop/{id}
"""
router = DefaultRouter()
router.register("shop", ShopViewSet, "shop")
router.register("address", AddressViewSet, "address")
router.register("model_shop", ShopModelViewSet, "model_shop")
router.register("model_address", AddressModelViewSet, "model_address")
urlpatterns = router.urls
