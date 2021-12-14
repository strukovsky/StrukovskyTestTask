from rest_framework.viewsets import ModelViewSet

from .models import Shop, Address
from .serializers import ShopSerializer, AddressSerializer

"""
These viewsets were created at the beginning of completing task.
I've decided to make them presented in the final version of my app
because they provide wide functionality which can be necessary in the future.

For example, if there's necessity of create Shop with not-null initial last_changed value
"""


class ShopViewSet(ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()


class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
