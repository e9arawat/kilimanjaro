# Generated by Django 4.2.9 on 2024-03-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kilimanjaro", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="slug",
            field=models.SlugField(),
        ),
    ]
