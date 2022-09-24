# Generated by Django 4.1.1 on 2022-09-23 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lists", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="list",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lists",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]