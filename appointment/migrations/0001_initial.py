# Generated by Django 5.1.3 on 2024-12-25 14:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("college_id", models.CharField(max_length=10, unique=True)),
                ("department", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "user_type",
                    models.CharField(
                        choices=[("professor", "Professor"), ("student", "Student")],
                        max_length=10,
                    ),
                ),
                ("password", models.CharField(max_length=15)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Professor",
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
                ("name", models.CharField(max_length=100)),
                ("college_id", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("department", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=15)),
                (
                    "user_type",
                    models.CharField(
                        choices=[("professor", "Professor"), ("student", "Student")],
                        default="professor",
                        max_length=10,
                    ),
                ),
                (
                    "custom_user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
