# Generated by Django 5.2 on 2025-04-15 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="turma",
            name="periodo",
            field=models.CharField(
                choices=[
                    ("MANHA", "Manhã"),
                    ("TARDE", "Tarde"),
                    ("INTEGRAL", "Integral"),
                ],
                max_length=50,
            ),
        ),
    ]
