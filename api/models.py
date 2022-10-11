from django.db import models


class Data(models.Model):
    color = models.CharField(max_length=30)
    price = models.DecimalField(default=100, decimal_places=2, max_digits=10)
    info = models.ForeignKey('api.CarType', on_delete=models.CASCADE, related_name='data')


class CarType(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    type = models.ForeignKey('api.Car', on_delete=models.CASCADE, related_name='car')

    def __str__(self):
        return self.name


class Car(models.Model):
    type = [
        ('Light', 'Light'),
        ('Normal', 'Normal'),
        ('Heavy', 'Heavy')
    ]
    car_type = models.CharField(max_length=10, choices=type)

    def __str__(self):
        return self.car_type

