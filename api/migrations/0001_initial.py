# Generated by Django 4.2.1 on 2023-05-15 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Esporte",
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
                ("nome_esporte", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Time",
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
                ("nome_time", models.CharField(max_length=100)),
                ("data_criacao", models.DateField(auto_now_add=True)),
                (
                    "nome_esporte",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.esporte"
                    ),
                ),
            ],
        ),
    ]
