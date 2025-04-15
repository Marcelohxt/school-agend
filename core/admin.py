from django.contrib import admin
from .models import Turma, Aluno, Atividade, Comunicado

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'periodo', 'professor', 'data_criacao')
    list_filter = ('ano', 'periodo')
    search_fields = ('nome', 'professor__username')

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'responsavel', 'turma', 'telefone')
    list_filter = ('turma',)
    search_fields = ('nome', 'responsavel', 'email')

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'turma', 'data', 'hora_inicio', 'hora_fim', 'professor')
    list_filter = ('tipo', 'turma', 'data')
    search_fields = ('descricao', 'turma__nome')

@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_envio', 'data_validade', 'autor', 'importante')
    list_filter = ('importante', 'data_envio', 'data_validade')
    search_fields = ('titulo', 'conteudo')
    filter_horizontal = ('turmas',)
