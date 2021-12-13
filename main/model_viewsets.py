from rest_framework.viewsets import ModelViewSet

from .models import Shop, Address
from .serializers import ShopSerializer, AddressSerializer

"""
Эти вьюсеты были созданы мною в первой версии тестового задания, чтобы проверить,
все ли корректно работает.

По-хорошему, их надо было удалить, но я решил их оставить, просто на случай,
если нужно будет выполнить что-то, чего не было в задании.
Например, если нужно будет добавить магазин с датой last_changed, отличной от сегодняшней

Эти вьюсеты в роутере имеют URL /model_shop/ и /model_address/ соответственно
"""


class ShopViewSet(ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()


class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
