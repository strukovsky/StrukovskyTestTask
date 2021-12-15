from datetime import datetime, timezone
from rest_framework.fields import DateTimeField, SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField
from .models import Shop, Address
"""
 ModelSerializer is used because I consider it quite suitable in this task
"""


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ShopSerializer(ModelSerializer):

    pretty_address = SerializerMethodField('prettify_address')
    last_changed = DateTimeField()
    
    def prettify_address(self, shop: Shop) -> str:
        address = shop.address
        return f"{address.street} {address.home}"

    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(ShopSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Shop
        fields = ('id', 'name', 'pretty_address', 'last_changed')
        
    

