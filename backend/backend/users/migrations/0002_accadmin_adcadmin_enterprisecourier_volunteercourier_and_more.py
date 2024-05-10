# Generated by Django 4.2.9 on 2024-03-08 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ACCAdmin",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("acc_name", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
            bases=("users.user",),
        ),
        migrations.CreateModel(
            name="ADCAdmin",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("adc_name", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
            bases=("users.user",),
        ),
        migrations.CreateModel(
            name="EnterpriseCourier",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("company_name", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=20)),
                ("company_address", models.TextField()),
                ("date_of_establishment", models.DateField()),
                ("number_of_light_duty", models.IntegerField()),
                ("number_of_medium_duty", models.IntegerField()),
                ("number_of_heavy_duty", models.IntegerField()),
                ("trade_registration_number", models.TextField()),
            ],
            options={
                "abstract": False,
            },
            bases=("users.user",),
        ),
        migrations.CreateModel(
            name="VolunteerCourier",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("full_name", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=20)),
                ("car_plate_number", models.CharField(max_length=20)),
                ("national_id_number", models.CharField(max_length=50)),
                ("city", models.TextField()),
                ("country", models.TextField()),
                ("vehicle_size", models.TextField()),
                ("availability", models.TextField()),
            ],
            options={
                "abstract": False,
            },
            bases=("users.user",),
        ),
        migrations.AlterModelOptions(
            name="user",
            options={},
        ),
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="user",
            name="date_joined",
        ),
        migrations.RemoveField(
            model_name="user",
            name="name",
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]