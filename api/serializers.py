from rest_framework import serializers
from .models import Car, CarType, Data


class DataSerializers(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['price', 'color']


class CarTypeSerializers(serializers.ModelSerializer):
    data = DataSerializers(many=True)

    class Meta:
        model = CarType
        fields = ['name', 'data']


class CarSerializer(serializers.ModelSerializer):
    car = CarTypeSerializers(many=True)

    class Meta:
        model = Car
        fields = ['car_type', 'car']
