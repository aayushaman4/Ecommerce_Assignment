from rest_framework import serializers
from .models import Product, Ip

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class IpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ip
        fields = '__all__'
        
    def create(self, validated_data):
        ip = Ip.objects.create(**validated_data)
        return ip