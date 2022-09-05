# Generated by Django 4.1 on 2022-09-05 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0005_amenity_facility_houserule_remove_room_room_type_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="amenity",
            options={"verbose_name_plural": "Ameities"},
        ),
        migrations.AlterModelOptions(
            name="facility",
            options={"verbose_name_plural": "Facilities"},
        ),
        migrations.AlterModelOptions(
            name="houserule",
            options={"verbose_name": "House Rule"},
        ),
        migrations.AlterModelOptions(
            name="roomtype",
            options={"verbose_name": "Room Type"},
        ),
        migrations.AlterField(
            model_name="room",
            name="amenities",
            field=models.ManyToManyField(blank=True, to="rooms.amenity"),
        ),
        migrations.AlterField(
            model_name="room",
            name="facilities",
            field=models.ManyToManyField(blank=True, to="rooms.facility"),
        ),
        migrations.AlterField(
            model_name="room",
            name="house_rules",
            field=models.ManyToManyField(blank=True, to="rooms.houserule"),
        ),
        migrations.CreateModel(
            name="Photo",
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
                ("caption", models.CharField(max_length=80)),
                ("file", models.ImageField(upload_to="")),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rooms.room"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
