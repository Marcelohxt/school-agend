# Generated by Django 5.0.2 on 2025-04-15 17:04

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20250415_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='nacionalidade',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='naturalidade',
        ),
        migrations.AddField(
            model_name='aluno',
            name='tipo_sanguineo',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3, null=True, verbose_name='Tipo Sanguíneo'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Aluno Ativo'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.RegexValidator(message='Formato do CPF deve ser XXX.XXX.XXX-XX', regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$')], verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de Criação'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='endereco',
            field=models.TextField(blank=True, verbose_name='Endereço Completo'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='alunos/', verbose_name='Foto do Aluno'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='observacoes',
            field=models.TextField(blank=True, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='professor_auxiliar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alunos_auxiliar', to='core.professor'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='professor_titular',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alunos_titular', to='core.professor'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='responsavel',
            field=models.CharField(max_length=100, verbose_name='Nome do Responsável'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='rg',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(max_length=15, verbose_name='Telefone de Contato'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alunos', to='core.turma'),
        ),
    ]
