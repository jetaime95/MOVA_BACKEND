# Generated by Django 4.1.3 on 2022-12-07 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="image",
            field=models.ImageField(max_length=255, null=True, upload_to="user/"),
        ),
    ]
