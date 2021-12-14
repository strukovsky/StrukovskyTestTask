import datetime

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .serializers import ShopSerializer, AddressSerializer
from .models import Shop, Address

"""
Эти вьюсете в роутере имеют путь /shop/ и /address/. Они содержат
все указанные в задании эндпойнты а потому, при проверке моего задания предпочтительны именно они.
"""


class ShopViewSet(ViewSet):
    """
    Вьюсет для магазина. Все эндпойнты — стандартные DRF эндпойнты
    """

    def list(self, request: Request) -> Response:
        queryset = Shop.objects.all()
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: Request, pk=None) -> Response:
        queryset = Shop.objects.all()
        shop = get_object_or_404(queryset, pk=pk)
        serializer = ShopSerializer(shop, many=False)
        return Response(serializer.data)

    def create(self, request: Request) -> Response:
        request_data = request.data
        address_id = request_data['address']
        request_data['address'] = get_object_or_404(Address, pk=address_id)
        shop = Shop(**request_data)
        shop.save()
        response_data = {
            "id": shop.id,
            "name": shop.name
        }
        return Response(response_data)

    def partial_update(self, request: Request, pk=None) -> Response:
        shop = get_object_or_404(Shop, pk=pk)
        data = request.data
        address = data['address']
        shop.address = get_object_or_404(Address, pk=address)
        shop.last_changed = datetime.date.today()
        serializer = ShopSerializer(shop)
        return Response(serializer.data)


class AddressViewSet(ViewSet):
    """
    Вьюсет для адресов. Все стандартное, кроме мною добавленного
    shops (его URL: /address/1/shops/), который возвращает магазины, принадлежащие адресу.
    """

    def list(self, request: Request) -> Response:
        queryset = Address.objects.all()
        serializer = AddressSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: Request, pk=None) -> Response:
        queryset = Address.objects.all()
        address = get_object_or_404(queryset, pk=pk)
        serializer = AddressSerializer(address, many=False)
        return Response(serializer.data)

    def create(self, request: Request) -> Response:
        address = Address(**request.data)
        address.save()
        return Response({"id": address.id})

    @action(methods=['GET'], detail=True)
    def shops(self, request: Request, pk=None) -> Response:
        """
        Найти магазины по заданному адресу
        Созданный мною GET эндпоинт, URL которого выглядит так:
        /address/1/shops
        Вместо единицы может быть любой интересующий айди адреса, по которому нужно найти магазины
        :param request: запрос
        :param pk: айди адреса
        :return: список магазинов по адресу
        """
        queryset = Shop.objects.filter(address_id=pk)
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)
