# Generated by Django 4.2.9 on 2024-04-17 18:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("aid", "0007_accaid_standard_stock_accaid_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="accaid",
            name="standard_stock",
        ),
    ]
