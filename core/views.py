from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Turma, Aluno, Atividade, Comunicado
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import TurmaForm, AlunoForm, AtividadeForm, ComunicadoForm

@login_required
def test_view(request):
    return render(request, 'core/test.html')

# Create your views here.

@login_required
def home(request):
    # Data atual
    hoje = timezone.now().date()
    
    # Estatísticas
    context = {
        'total_alunos': Aluno.objects.count(),
        'total_turmas': Turma.objects.count(),
        'atividades_hoje': Atividade.objects.filter(data=hoje).count(),
        'comunicados_ativos': Comunicado.objects.filter(data_validade__gte=hoje).count(),
        
        # Comunicados recentes
        'comunicados_recentes': Comunicado.objects.filter(
            data_validade__gte=hoje
        ).order_by('-data_envio')[:5],
        
        # Atividades do dia
        'atividades_do_dia': Atividade.objects.filter(
            data=hoje
        ).order_by('hora_inicio')[:5],
    }
    
    # Calendário da semana
    dias_semana = []
    horarios = ['07:00', '08:00', '09:00', '10:00', '11:00', 
                '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']
    
    # Pega os próximos 5 dias úteis
    data_atual = hoje
    while len(dias_semana) < 5:
        if data_atual.weekday() < 5:  # 0-4 são dias úteis (seg-sex)
            dias_semana.append(data_atual.strftime('%A'))
        data_atual += timedelta(days=1)
    
    # Atividades da semana
    fim_semana = hoje + timedelta(days=5)
    atividades_semana = Atividade.objects.filter(
        data__range=[hoje, fim_semana]
    ).order_by('data', 'hora_inicio')
    
    context.update({
        'dias_semana': dias_semana,
        'horarios': horarios,
        'atividades_semana': atividades_semana,
    })
    
    return render(request, 'home.html', context)

@login_required
def turmas(request):
    turmas = Turma.objects.all()
    context = {
        'object_list': turmas,
        'title': 'Turmas',
        'create_url': 'turma_create',
        'create_text': 'Nova Turma',
        'headers': ['Nome', 'Ano', 'Período', 'Professor']
    }
    return render(request, 'core/turmas.html', context)

@login_required
def turma_create(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            turma = form.save()
            messages.success(request, 'Turma criada com sucesso!')
            return redirect('turmas')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = TurmaForm()
    
    context = {
        'form': form,
        'title': 'Nova Turma',
        'list_url': 'turmas'
    }
    return render(request, 'core/turma_form.html', context)

@login_required
def turma_edit(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Turma atualizada com sucesso!')
            return redirect('turmas')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = TurmaForm(instance=turma)
    
    context = {
        'form': form,
        'title': 'Editar Turma',
        'list_url': 'turmas'
    }
    return render(request, 'core/turma_form.html', context)

@login_required
def turma_delete(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    if request.method == 'POST':
        turma.delete()
        messages.success(request, 'Turma excluída com sucesso!')
        return redirect('turmas')
    return render(request, 'turma_confirm_delete.html', {'turma': turma})

@login_required
def alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos.html', {'alunos': alunos})

@login_required
def aluno_create(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno criado com sucesso!')
            return redirect('alunos')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = AlunoForm()
    
    context = {
        'form': form,
        'title': 'Novo Aluno',
        'turmas': Turma.objects.all(),
        'list_url': 'alunos'
    }
    return render(request, 'core/aluno_form.html', context)

@login_required
def aluno_edit(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno atualizado com sucesso!')
            return redirect('alunos')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = AlunoForm(instance=aluno)
    
    context = {
        'form': form,
        'title': 'Editar Aluno',
        'turmas': Turma.objects.all(),
        'list_url': 'alunos'
    }
    return render(request, 'core/aluno_form.html', context)

@login_required
def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        messages.success(request, 'Aluno excluído com sucesso!')
        return redirect('alunos')
    return render(request, 'aluno_confirm_delete.html', {'aluno': aluno})

@login_required
def atividades(request):
    atividades = Atividade.objects.all().order_by('data', 'hora_inicio')
    return render(request, 'atividades.html', {'atividades': atividades})

@login_required
def atividade_create(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Atividade criada com sucesso!')
            return redirect('atividades')
    else:
        form = AtividadeForm()
    return render(request, 'atividade_form.html', {'form': form, 'title': 'Nova Atividade'})

@login_required
def atividade_edit(request, pk):
    atividade = get_object_or_404(Atividade, pk=pk)
    if request.method == 'POST':
        form = AtividadeForm(request.POST, instance=atividade)
        if form.is_valid():
            form.save()
            messages.success(request, 'Atividade atualizada com sucesso!')
            return redirect('atividades')
    else:
        form = AtividadeForm(instance=atividade)
    return render(request, 'atividade_form.html', {'form': form, 'title': 'Editar Atividade'})

@login_required
def atividade_delete(request, pk):
    atividade = get_object_or_404(Atividade, pk=pk)
    if request.method == 'POST':
        atividade.delete()
        messages.success(request, 'Atividade excluída com sucesso!')
        return redirect('atividades')
    return render(request, 'atividade_confirm_delete.html', {'atividade': atividade})

@login_required
def comunicados(request):
    comunicados = Comunicado.objects.all().order_by('-data_envio')
    return render(request, 'comunicados.html', {'comunicados': comunicados})

@login_required
def comunicado_create(request):
    if request.method == 'POST':
        form = ComunicadoForm(request.POST)
        if form.is_valid():
            comunicado = form.save(commit=False)
            comunicado.data_envio = timezone.now()
            comunicado.save()
            messages.success(request, 'Comunicado criado com sucesso!')
            return redirect('comunicados')
    else:
        form = ComunicadoForm()
    return render(request, 'comunicado_form.html', {'form': form, 'title': 'Novo Comunicado'})

@login_required
def comunicado_edit(request, pk):
    comunicado = get_object_or_404(Comunicado, pk=pk)
    if request.method == 'POST':
        form = ComunicadoForm(request.POST, instance=comunicado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comunicado atualizado com sucesso!')
            return redirect('comunicados')
    else:
        form = ComunicadoForm(instance=comunicado)
    return render(request, 'comunicado_form.html', {'form': form, 'title': 'Editar Comunicado'})

@login_required
def comunicado_delete(request, pk):
    comunicado = get_object_or_404(Comunicado, pk=pk)
    if request.method == 'POST':
        comunicado.delete()
        messages.success(request, 'Comunicado excluído com sucesso!')
        return redirect('comunicados')
    return render(request, 'comunicado_confirm_delete.html', {'comunicado': comunicado})

@login_required
def profile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('profile')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'profile.html', {'form': form})

@login_required
def settings(request):
    return render(request, 'settings.html')
