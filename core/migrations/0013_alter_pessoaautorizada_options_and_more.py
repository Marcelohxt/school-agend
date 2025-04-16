# Generated by Django 5.0.2 on 2025-04-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_aluno_estado_civil_mae_aluno_estado_civil_pai_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pessoaautorizada',
            options={'verbose_name': 'Pessoa Autorizada', 'verbose_name_plural': 'Pessoas Autorizadas'},
        ),
        migrations.RemoveField(
            model_name='pessoaautorizada',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='pessoaautorizada',
            name='foto_documento',
        ),
        migrations.AddField(
            model_name='pessoaautorizada',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to='documentos_autorizados/'),
        ),
        migrations.AlterField(
            model_name='pessoaautorizada',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='pessoaautorizada',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_autorizados/'),
        ),
        migrations.AlterField(
            model_name='pessoaautorizada',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pessoaautorizada',
            name='parentesco',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pessoaautorizada',
            name='rg',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
