# Generated by Django 5.0.2 on 2025-04-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_pessoaautorizada_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(blank=True, default='', max_length=14, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='rg',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='RG'),
        ),
    ]
