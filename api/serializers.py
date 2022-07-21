from rest_framework import serializers
from base.models import Item

class ItemSeriliazers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'