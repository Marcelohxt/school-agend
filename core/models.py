from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Turma(models.Model):
    PERIODO_CHOICES = [
        ('MANHA', 'Manhã'),
        ('TARDE', 'Tarde'),
        ('INTEGRAL', 'Integral'),
    ]

    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    periodo = models.CharField(max_length=50, choices=PERIODO_CHOICES)
    professor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='turmas')
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nome} - {self.periodo}"

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    responsavel = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, related_name='alunos')
    foto = models.ImageField(upload_to='alunos/', null=True, blank=True)
    observacoes = models.TextField(blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

class Atividade(models.Model):
    TIPO_CHOICES = [
        ('AULA', 'Aula'),
        ('RECREIO', 'Recreio'),
        ('ALMOCO', 'Almoço'),
        ('SONO', 'Sono'),
        ('OUTRO', 'Outro'),
    ]

    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='atividades')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    descricao = models.TextField()
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    professor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='atividades')
    observacoes = models.TextField(blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.turma} - {self.data}"

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

class Comunicado(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_envio = models.DateTimeField(default=timezone.now)
    data_validade = models.DateField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comunicados')
    turmas = models.ManyToManyField(Turma, related_name='comunicados')
    importante = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Comunicado'
        verbose_name_plural = 'Comunicados'
