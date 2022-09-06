# Generated by Django 4.1 on 2022-09-06 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("rooms", "0001_initial"),
        ("lists", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="list",
            name="rooms",
            field=models.ManyToManyField(
                blank=True, related_name="lists", to="rooms.room"
            ),
        ),
    ]