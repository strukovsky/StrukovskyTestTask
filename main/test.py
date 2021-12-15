from datetime import datetime
from rest_framework.test import APIRequestFactory
from django.test import TestCase
from .viewsets import ShopViewSet, AddressViewSet
from .models import Shop, Address
from rest_framework.settings import api_settings

factory = APIRequestFactory()


class AddressTestCase(TestCase):
    def setUp(self) -> None:
        address = Address.objects.create(street="Test", home=1)
        Address.objects.create(street="Another test", home=3)
        Shop.objects.create(address=address, name="Test shop")
        Shop.objects.create(address=address, name="Test shop 2")
        return super().setUp()

    def test_get_all_addresses(self):
        address = AddressViewSet()
        request = factory.get('/address/', format='json')
        response = address.list(request=request)
        self.assertEqual(200, response.status_code)
        response_data = list(map(dict, response.data))
        expected = [{
            'id': 1,
            'street': 'Test',
            'home': 1
        }, {
            'id': 2,
            'street': 'Another test',
            'home': 3
        }]
        self.assertEqual(expected, response_data)

    def test_get_address_details(self):
        address = AddressViewSet()
        request = factory.get('/address/1/', format='json')
        response = address.retrieve(request=request, pk=1)
        self.assertEqual(200, response.status_code)
        response_data = dict(response.data)
        expected = {'id': 1, 'street': 'Test', 'home': 1}
        self.assertEqual(expected, response_data)

    def test_create_new_address(self):
        address = AddressViewSet()
        request = factory.post('/address/')
        request.data = {'street': 'Yunosti', 'home': 15}
        response = address.create(request)
        self.assertEqual(200, response.status_code)
        self.assertEqual({'id': 3}, dict(response.data))

        validate_creating = factory.get('/address/3/')
        validate_response = address.retrieve(validate_creating, pk=3)
        self.assertEqual(200, validate_response.status_code)
        response_data = dict(validate_response.data)
        self.assertEqual(response_data, {
            'id': 3,
            'street': 'Yunosti',
            'home': 15
        })

    def test_get_shops_of_address(self):
        address = AddressViewSet()
        request = factory.get('/address/1/shops/')
        response = address.shops(request=request, pk=1)
        self.assertEqual(200, response.status_code)
        actual = list(map(dict, response.data))
        self.assertEqual(2, len(actual))
        # self.assertEqual(expected, actual)


class ShopTestCase(TestCase):
    def setUp(self) -> None:
        address = Address.objects.create(street="Test", home=1)
        Address.objects.create(street="Another test", home=3)
        Shop.objects.create(address=address, name="Test shop")
        Shop.objects.create(address=address, name="Test shop 2")

        return super().setUp()

    def test_get_all_shops(self):
        shop = ShopViewSet()
        request = factory.get('/shop/', format='json')
        response = shop.list(request=request)
        self.assertEqual(response.status_code, 200)
        response_data = list(map(dict, response.data))
        self.assertEqual(2, len(response_data))

    def test_get_shop_details(self):
        shop = ShopViewSet()
        request = factory.get('/shop/1/', format='json')
        response = shop.retrieve(request=request, pk=1)
        self.assertEqual(200, response.status_code)
        response_data = dict(response.data)
        shop_to_validate = Shop.objects.get(pk=1)
        last_changed: datetime = shop_to_validate.last_changed
        formatted_last_changed_with_tz = datetime.strftime(
            last_changed, api_settings.DATETIME_FORMAT)
        self.assertEqual(formatted_last_changed_with_tz,
                         response_data.get('last_changed'))

    def test_create_new_shop(self):
        shop = ShopViewSet()
        request = factory.post('/shop/')
        request.data = {'address': 1, 'name': 'Test added shop'}
        response = shop.create(request=request)
        self.assertEqual(200, response.status_code)
        self.assertEqual({
            'id': 3,
            'name': 'Test added shop'
        }, dict(response.data))

        validate_creating = factory.get('/shop/3/')
        validate_response = shop.retrieve(validate_creating, pk=3)
        self.assertEqual(200, validate_response.status_code)
        response_data = dict(validate_response.data)
        expected = {
            'id': 3,
            'name': 'Test added shop',
            'pretty_address': 'Test 1',
            'last_changed':
            datetime.now().strftime(api_settings.DATETIME_FORMAT)
        }
        self.assertEqual(expected, response_data)

    def test_change_shop_address(self):
        shop = ShopViewSet()
        request = factory.patch('/shop/1/')
        request.data = {'address': 2}
        response = shop.partial_update(request=request, pk=1)
        self.assertEqual(200, response.status_code)
        # response received on request to change shop's data
        changing_response = dict(response.data)
        changing_timestamp = changing_response.get('last_changed')

        request_validate_changes = factory.get('/shop/1/')
        response_validate_changes = shop.retrieve(
            request=request_validate_changes, pk=1)
        response_data = dict(response_validate_changes.data)
        last_changed_from_validate = response_data['last_changed']
        self.assertEqual(changing_timestamp, last_changed_from_validate)
