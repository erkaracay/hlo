# Generated by Django 4.2.9 on 2024-04-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aid", "0011_aidtyperequest"),
    ]

    operations = [
        migrations.AddField(
            model_name="aidtype",
            name="volume",
            field=models.IntegerField(default=0, verbose_name="Volume"),
            preserve_default=False,
        ),
    ]
