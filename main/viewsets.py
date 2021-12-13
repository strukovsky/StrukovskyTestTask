from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .serializers import ShopSerializer, AddressSerializer
from .models import Shop, Address


class ShopViewSet(ViewSet):

    def list(self, request):
        queryset = Shop.objects.all()
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Shop.objects.all()
        shop = get_object_or_404(queryset, pk=pk)
        serializer = ShopSerializer(shop, many=False)
        return Response(serializer.data)


class AddressViewSet(ViewSet):

    def list(self, request):
        queryset = Address.objects.all()
        serializer = AddressSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Address.objects.all()
        address = get_object_or_404(queryset, pk=pk)
        serializer = AddressSerializer(address, many=False)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def shops(self, request, pk):
        queryset = Shop.objects.filter(address_id=pk)
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)
