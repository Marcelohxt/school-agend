from django import forms
from .models import Turma, Aluno, Atividade, Comunicado, Professor, PessoaAutorizada
from django.contrib.auth.models import User

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'ano', 'periodo', 'professor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'periodo': forms.Select(attrs={'class': 'form-select'}),
            'professor': forms.Select(attrs={'class': 'form-select'}),
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
        fields = [
            'nome', 'data_nascimento', 'sexo', 'tipo_sanguineo', 'cpf', 'rg',
            'nome_pai', 'telefone_pai', 'profissao_pai', 'estado_civil_pai',
            'nome_mae', 'telefone_mae', 'profissao_mae', 'estado_civil_mae',
            'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado',
            'responsavel', 'telefone', 'email', 'foto', 'observacoes', 'turma',
            'professor_titular', 'professor_auxiliar', 'ativo'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control data-mask',
                    'placeholder': 'DD/MM/AAAA'
                },
                format='%d/%m/%Y'
            ),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'tipo_sanguineo': forms.Select(attrs={'class': 'form-select'}),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control cpf-mask',
                'placeholder': '000.000.000-00'
            }),
            'rg': forms.TextInput(attrs={
                'class': 'form-control rg-mask',
                'placeholder': '00.000.000-0'
            }),
            'nome_pai': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome completo do pai'
            }),
            'telefone_pai': forms.TextInput(attrs={
                'class': 'form-control telefone-mask',
                'placeholder': '(00) 00000-0000'
            }),
            'profissao_pai': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Profissão do pai'
            }),
            'estado_civil_pai': forms.Select(attrs={'class': 'form-select'}),
            'nome_mae': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome completo da mãe'
            }),
            'telefone_mae': forms.TextInput(attrs={
                'class': 'form-control telefone-mask',
                'placeholder': '(00) 00000-0000'
            }),
            'profissao_mae': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Profissão da mãe'
            }),
            'estado_civil_mae': forms.Select(attrs={'class': 'form-select'}),
            'cep': forms.TextInput(attrs={
                'class': 'form-control cep-mask',
                'placeholder': '00000-000'
            }),
            'logradouro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da rua'
            }),
            'numero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nº'
            }),
            'complemento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apto, Bloco, etc'
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do bairro'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da cidade'
            }),
            'estado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'UF',
                'maxlength': '2'
            }),
            'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control telefone-mask',
                'placeholder': '(00) 00000-0000'
            }),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'turma': forms.Select(attrs={'class': 'form-select'}),
            'professor_titular': forms.Select(attrs={'class': 'form-select'}),
            'professor_auxiliar': forms.Select(attrs={'class': 'form-select'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'nome': 'Nome do Aluno',
            'cpf': 'CPF',
            'rg': 'RG',
            'responsavel': 'Responsável',
            'telefone': 'Telefone',
            'email': 'Email',
            'turma': 'Turma',
            'professor_titular': 'Professor Titular',
            'professor_auxiliar': 'Professor Auxiliar',
            'foto': 'Foto do Aluno',
            'observacoes': 'Observações',
            'ativo': 'Aluno Ativo'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_nascimento'].input_formats = ['%d/%m/%Y', '%Y-%m-%d']
        self.fields['turma'].empty_label = 'Selecione a turma'
        self.fields['professor_titular'].queryset = Professor.objects.filter(tipo='TITULAR')
        self.fields['professor_titular'].empty_label = 'Selecione o professor titular'
        self.fields['professor_auxiliar'].queryset = Professor.objects.filter(tipo='AUXILIAR')
        self.fields['professor_auxiliar'].empty_label = 'Selecione o professor auxiliar'

class AtividadeForm(forms.ModelForm):
    data = forms.DateField(
        label='Data',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        ),
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        help_text='Formato: dd/mm/aaaa'
    )
    
    hora_inicio = forms.TimeField(
        label='Hora de Início',
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control',
                'type': 'time'
            }
        ),
        input_formats=['%H:%M'],
        help_text='Formato: HH:MM (24h)'
    )
    
    hora_fim = forms.TimeField(
        label='Hora de Término',
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control',
                'type': 'time'
            }
        ),
        input_formats=['%H:%M'],
        help_text='Formato: HH:MM (24h)'
    )

    class Meta:
        model = Atividade
        fields = ['data', 'hora_inicio', 'hora_fim', 'tipo', 'turma', 'descricao']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'turma': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ComunicadoForm(forms.ModelForm):
    data_validade = forms.DateField(
        label='Data de Validade',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        ),
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        help_text='Formato: dd/mm/aaaa'
    )

    class Meta:
        model = Comunicado
        fields = ['titulo', 'conteudo', 'data_validade']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'email', 'telefone', 'foto', 'turma', 'tipo', 'professor_titular']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do professor'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@exemplo.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000'
            }),
            'foto': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'turma': forms.Select(attrs={
                'class': 'form-select'
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'professor_titular': forms.Select(attrs={
                'class': 'form-select'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra apenas professores titulares para o campo professor_titular
        self.fields['professor_titular'].queryset = Professor.objects.filter(tipo='TITULAR')
        # Torna o campo professor_titular obrigatório apenas para auxiliares
        if self.instance and self.instance.tipo == 'AUXILIAR':
            self.fields['professor_titular'].required = True
        else:
            self.fields['professor_titular'].required = False

class PessoaAutorizadaForm(forms.ModelForm):
    cpf = forms.CharField(
        max_length=14,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '000.000.000-00'
        })
    )
    rg = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o RG'
        })
    )
    foto_documento = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = PessoaAutorizada
        fields = ['nome', 'telefone', 'cpf', 'rg', 'foto_documento', 'parentesco', 'foto', 'observacoes']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da pessoa autorizada'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000'
            }),
            'parentesco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Tio, Avó, Babá'
            }),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observações adicionais'
            }),
        }
        labels = {
            'nome': 'Nome',
            'telefone': 'Telefone',
            'foto': 'Foto da Pessoa',
            'foto_documento': 'Foto do Documento',
            'parentesco': 'Parentesco',
            'observacoes': 'Observações'
        } 