# Generated by Django 4.2.9 on 2024-05-05 20:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("logistics", "0006_enterprisetask_done"),
    ]

    operations = [
        migrations.RenameField(
            model_name="enterprisetask",
            old_name="destination",
            new_name="source",
        ),
        migrations.RenameField(
            model_name="volunteertask",
            old_name="destination",
            new_name="source",
        ),
        migrations.RemoveField(
            model_name="enterprisetask",
            name="done",
        ),
        migrations.RemoveField(
            model_name="volunteertask",
            name="code",
        ),
        migrations.RemoveField(
            model_name="volunteertask",
            name="done",
        ),
        migrations.AddField(
            model_name="enterprisetask",
            name="status",
            field=models.CharField(default=" ", max_length=100, verbose_name="Status"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="volunteertask",
            name="source_code",
            field=models.CharField(
                default=" ", editable=False, max_length=6, unique=True, verbose_name="Task Source Code"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="volunteertask",
            name="status",
            field=models.CharField(default=" ", max_length=100, verbose_name="Status"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="volunteertask",
            name="target_code",
            field=models.CharField(
                default=" ", editable=False, max_length=6, unique=True, verbose_name="Task Target Code"
            ),
            preserve_default=False,
        ),
    ]
