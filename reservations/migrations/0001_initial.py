# Generated by Django 4.1 on 2022-09-06 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reservation",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("confirmed", "Confirmed"),
                            ("canceled", "Canceled"),
                        ],
                        default="pending",
                        max_length=12,
                    ),
                ),
                ("check_in", models.DateField()),
                ("check_out", models.DateField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
