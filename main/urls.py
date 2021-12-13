from rest_framework.routers import DefaultRouter

from .model_viewsets import (
    ShopViewSet as ShopModelViewSet,
    AddressViewSet as AddressModelViewSet
)
from .viewsets import ShopViewSet, AddressViewSet
"""
В model_viewsets лежат вьюсеты, которые создаются классом ModelViewSet
Я их создавал для первой версии моего задания, но решил оставить на случай,
если потребуется какой-то функционал, выходящий за рамки условия задания. 

Выполненное задание находится по URL /shop/* и /address/* соответственно
"""
router = DefaultRouter()
router.register("shop", ShopViewSet, "shop")
router.register("address", AddressViewSet, "address")
router.register("model_shop", ShopModelViewSet, "model_shop")
router.register("model_address", AddressModelViewSet, "model_address")
urlpatterns = router.urls
