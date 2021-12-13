from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField
from .models import Shop, Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'last_changed', 'address']
        address = SlugRelatedField('address', many=False, read_only=True)
