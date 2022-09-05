# Generated by Django 4.1 on 2022-09-05 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0002_room_address_room_baths_room_bedrooms_room_beds_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="RoomType",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("update", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=30)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="room",
            name="room_type",
            field=models.ManyToManyField(blank=True, null=True, to="rooms.roomtype"),
        ),
    ]
