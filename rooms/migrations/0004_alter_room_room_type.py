# Generated by Django 4.1 on 2022-09-05 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0003_roomtype_room_room_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="room_type",
            field=models.ManyToManyField(blank=True, to="rooms.roomtype"),
        ),
    ]
