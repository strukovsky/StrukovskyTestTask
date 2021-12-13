from rest_framework.viewsets import ModelViewSet

from .models import Shop, Address
from .serializers import ShopSerializer, AddressSerializer


class ShopViewSet(ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()


class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
