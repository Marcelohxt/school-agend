from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator

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
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    
    TIPO_SANGUINEO_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    ESTADO_CIVIL_CHOICES = [
        ('SOLTEIRO', 'Solteiro(a)'),
        ('CASADO', 'Casado(a)'),
        ('DIVORCIADO', 'Divorciado(a)'),
        ('VIUVO', 'Viúvo(a)'),
        ('UNIAO_ESTAVEL', 'União Estável'),
    ]

    # Dados Pessoais
    nome = models.CharField("Nome Completo", max_length=100)
    data_nascimento = models.DateField("Data de Nascimento")
    sexo = models.CharField("Sexo", max_length=1, choices=SEXO_CHOICES)
    tipo_sanguineo = models.CharField("Tipo Sanguíneo", max_length=3, choices=TIPO_SANGUINEO_CHOICES, blank=True, null=True)
    cpf = models.CharField(
        "CPF",
        max_length=14,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
                message="Formato do CPF deve ser XXX.XXX.XXX-XX"
            )
        ]
    )
    rg = models.CharField(
        "RG",
        max_length=20,
        blank=True,
        null=True
    )

    # Dados do Pai
    nome_pai = models.CharField("Nome do Pai", max_length=100, blank=True, null=True)
    telefone_pai = models.CharField("Telefone do Pai", max_length=15, blank=True, null=True)
    profissao_pai = models.CharField("Profissão do Pai", max_length=100, blank=True, null=True)
    estado_civil_pai = models.CharField("Estado Civil do Pai", max_length=20, choices=ESTADO_CIVIL_CHOICES, blank=True, null=True)

    # Dados da Mãe
    nome_mae = models.CharField("Nome da Mãe", max_length=100, blank=True, null=True)
    telefone_mae = models.CharField("Telefone da Mãe", max_length=15, blank=True, null=True)
    profissao_mae = models.CharField("Profissão da Mãe", max_length=100, blank=True, null=True)
    estado_civil_mae = models.CharField("Estado Civil da Mãe", max_length=20, choices=ESTADO_CIVIL_CHOICES, blank=True, null=True)

    # Endereço
    cep = models.CharField("CEP", max_length=9, blank=True, null=True)
    logradouro = models.CharField("Logradouro", max_length=200, blank=True, null=True)
    numero = models.CharField("Número", max_length=10, blank=True, null=True)
    complemento = models.CharField("Complemento", max_length=100, blank=True, null=True)
    bairro = models.CharField("Bairro", max_length=100, blank=True, null=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True, null=True)
    estado = models.CharField("Estado", max_length=2, blank=True, null=True)

    # Outros campos existentes...
    responsavel = models.CharField("Nome do Responsável", max_length=100)
    telefone = models.CharField("Telefone de Contato", max_length=15)
    email = models.EmailField("E-mail", blank=True, null=True)
    endereco = models.TextField("Endereço Completo", blank=True)
    turma = models.ForeignKey(
        'Turma',
        on_delete=models.SET_NULL,
        null=True,
        related_name='alunos'
    )
    professor_titular = models.ForeignKey(
        'Professor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='alunos_titular'
    )
    professor_auxiliar = models.ForeignKey(
        'Professor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='alunos_auxiliar'
    )
    foto = models.ImageField("Foto do Aluno", upload_to='alunos/', null=True, blank=True)
    observacoes = models.TextField("Observações", blank=True)
    data_criacao = models.DateTimeField("Data de Criação", default=timezone.now)
    ativo = models.BooleanField("Aluno Ativo", default=True)

    def __str__(self):
        return f"{self.nome} - {self.turma if self.turma else 'Sem Turma'}"

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ['nome']

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

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='professores/', null=True, blank=True)
    turma = models.ForeignKey('Turma', on_delete=models.SET_NULL, null=True, blank=True, related_name='professores')
    tipo = models.CharField(max_length=20, choices=[
        ('TITULAR', 'Professor Titular'),
        ('AUXILIAR', 'Professor Auxiliar')
    ], default='TITULAR')
    professor_titular = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='auxiliares')

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} - {self.get_tipo_display()}"

class PessoaAutorizada(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='pessoas_autorizadas')
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    parentesco = models.CharField(max_length=50)
    documento = models.FileField(upload_to='documentos_autorizados/', blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_autorizados/', blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.parentesco}"

    class Meta:
        verbose_name = 'Pessoa Autorizada'
        verbose_name_plural = 'Pessoas Autorizadas'
