from django import forms
from .models import Turma, Aluno, Atividade, Comunicado
from django.contrib.auth.models import User

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'ano', 'periodo', 'professor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
            'ano': forms.NumberInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
            'periodo': forms.Select(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
            'professor': forms.Select(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
        }
        labels = {
            'nome': 'Nome da Turma',
            'ano': 'Ano',
            'periodo': 'Período',
            'professor': 'Professor',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['professor'].queryset = User.objects.filter(is_staff=True)
        self.fields['professor'].empty_label = 'Selecione o professor'

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'data_nascimento', 'responsavel', 'telefone', 'email', 'turma', 'foto', 'observacoes']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500', 'type': 'date'}),
            'responsavel': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
            'telefone': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
            'email': forms.EmailInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
            'turma': forms.Select(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
            'foto': forms.FileInput(attrs={'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'}),
            'observacoes': forms.Textarea(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500', 'rows': 3}),
        }
        labels = {
            'nome': 'Nome do Aluno',
            'data_nascimento': 'Data de Nascimento',
            'responsavel': 'Responsável',
            'telefone': 'Telefone',
            'email': 'Email',
            'turma': 'Turma',
            'foto': 'Foto do Aluno',
            'observacoes': 'Observações',
        }

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['data', 'hora_inicio', 'hora_fim', 'tipo', 'turma', 'descricao']
        widgets = {
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'hora_fim': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'turma': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ComunicadoForm(forms.ModelForm):
    class Meta:
        model = Comunicado
        fields = ['titulo', 'conteudo', 'data_validade']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'data_validade': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        } 