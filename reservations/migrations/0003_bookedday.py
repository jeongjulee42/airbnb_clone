# Generated by Django 4.1.1 on 2022-09-19 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookedDay",
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
                ("day", models.DateField()),
                (
                    "reservation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reservations.reservation",
                    ),
                ),
            ],
            options={
                "verbose_name": "Booked Day",
                "verbose_name_plural": "Booked Days",
            },
        ),
    ]
