from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField
from .models import Shop, Address

"""
Использую ModelSerializer
"""


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ShopSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(ShopSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Shop
        fields = '__all__'
        address = SlugRelatedField('address', many=False, read_only=True)
