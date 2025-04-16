# Generated by Django 5.0.2 on 2025-04-15 16:17

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_aluno_cpf_alter_aluno_rg'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={'ordering': ['nome'], 'verbose_name': 'Aluno', 'verbose_name_plural': 'Alunos'},
        ),
        migrations.AddField(
            model_name='aluno',
            name='ativo',
            field=models.BooleanField(default=True, help_text='Indica se o aluno está ativo na escola', verbose_name='Aluno Ativo'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='cep',
            field=models.CharField(blank=True, help_text='Formato: XXXXX-XXX', max_length=9, null=True, validators=[django.core.validators.RegexValidator(message='Formato do CEP deve ser XXXXX-XXX', regex='^\\d{5}-\\d{3}$')], verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='cidade',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='endereco',
            field=models.TextField(blank=True, help_text='Rua, número, complemento, bairro', verbose_name='Endereço Completo'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='estado',
            field=models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, null=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='nacionalidade',
            field=models.CharField(blank=True, default='Brasileira', max_length=50, null=True, verbose_name='Nacionalidade'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='naturalidade',
            field=models.CharField(blank=True, help_text='Cidade onde nasceu', max_length=50, null=True, verbose_name='Naturalidade'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(blank=True, help_text='Formato: XXX.XXX.XXX-XX', max_length=14, null=True, validators=[django.core.validators.RegexValidator(message='Formato do CPF deve ser XXX.XXX.XXX-XX', regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$')], verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Data de Criação'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(help_text='Formato: DD/MM/AAAA', verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.EmailField(blank=True, help_text='E-mail para contato', max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, help_text='Foto atual do aluno', null=True, upload_to='alunos/', verbose_name='Foto do Aluno'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(help_text='Digite o nome completo do aluno', max_length=100, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='observacoes',
            field=models.TextField(blank=True, help_text='Informações adicionais relevantes', verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='professor_auxiliar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alunos_auxiliar', to='core.professor', verbose_name='Professor Auxiliar'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='professor_titular',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alunos_titular', to='core.professor', verbose_name='Professor Titular'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='responsavel',
            field=models.CharField(help_text='Nome completo do responsável principal', max_length=100, verbose_name='Nome do Responsável'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='rg',
            field=models.CharField(blank=True, help_text='Digite o RG completo com dígito verificador', max_length=20, null=True, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(help_text='Formato: (XX) XXXXX-XXXX', max_length=15, validators=[django.core.validators.RegexValidator(message='Formato do telefone deve ser (XX) XXXXX-XXXX', regex='^\\(\\d{2}\\) \\d{5}-\\d{4}$')], verbose_name='Telefone de Contato'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alunos', to='core.turma', verbose_name='Turma'),
        ),
    ]
