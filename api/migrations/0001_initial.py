# Generated by Django 4.1.2 on 2022-10-11 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "car_type",
                    models.CharField(
                        choices=[("Light", "LG"), ("Normal", "NM"), ("Heavy", "HV")],
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CarType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=25)),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="car",
                        to="api.car",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("color", models.CharField(max_length=30)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=100, max_digits=10),
                ),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="data",
                        to="api.cartype",
                    ),
                ),
            ],
        ),
    ]