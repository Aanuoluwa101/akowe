# Generated by Django 5.0.1 on 2024-03-28 07:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Officiator",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("rank", models.CharField(max_length=70)),
                ("phone", models.CharField(max_length=15)),
                ("can_conduct_on_weekdays", models.BooleanField()),
                ("can_conduct_on_sundays", models.BooleanField()),
                ("can_read_on_weekdays", models.BooleanField()),
                ("can_read_on_sundays", models.BooleanField()),
                ("can_preach_on_weekdays", models.BooleanField()),
                ("can_preach_on_sundays", models.BooleanField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("last_modified", models.DateTimeField(auto_now=True)),
                (
                    "secretary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="officiators",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]