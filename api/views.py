from rest_framework import viewsets
from .serializers import *
from .models import *


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarTypeViewSet(viewsets.ModelViewSet):
    serializer_class = CarTypeSerializers
    queryset = CarType.objects.all()


class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataSerializers
    queryset = Data.objects.all()