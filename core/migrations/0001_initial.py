# Generated by Django 4.1.3 on 2022-12-03 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hotel",
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
                ("name", models.CharField(max_length=255)),
                ("price", models.FloatField()),
                ("image", models.ImageField(upload_to="")),
                ("description", models.TextField()),
            ],
        ),
    ]
