# Generated by Django 4.1.1 on 2022-09-14 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_email_confirmed_user_email_secret"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="email_confirmed",
            new_name="email_verified",
        ),
        migrations.AlterField(
            model_name="user",
            name="email_secret",
            field=models.CharField(blank=True, default="", max_length=20),
        ),
    ]
