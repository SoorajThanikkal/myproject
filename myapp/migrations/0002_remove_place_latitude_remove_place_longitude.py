# Generated by Django 4.2.6 on 2024-03-07 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="place", name="latitude",),
        migrations.RemoveField(model_name="place", name="longitude",),
    ]