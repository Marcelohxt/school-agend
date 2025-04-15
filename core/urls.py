from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Test URL
    path('test/', views.test_view, name='test'),
    
    # Turmas URLs
    path('turmas/', views.turmas, name='turmas'),
    path('turmas/nova/', views.turma_create, name='turma_create'),
    path('turmas/<int:pk>/editar/', views.turma_edit, name='turma_edit'),
    path('turmas/<int:pk>/excluir/', views.turma_delete, name='turma_delete'),
    
    # Alunos URLs
    path('alunos/', views.alunos, name='alunos'),
    path('alunos/novo/', views.aluno_create, name='aluno_create'),
    path('alunos/<int:pk>/editar/', views.aluno_edit, name='aluno_edit'),
    path('alunos/<int:pk>/excluir/', views.aluno_delete, name='aluno_delete'),
    
    # Atividades URLs
    path('atividades/', views.atividades, name='atividades'),
    path('atividades/nova/', views.atividade_create, name='atividade_create'),
    path('atividades/<int:pk>/editar/', views.atividade_edit, name='atividade_edit'),
    path('atividades/<int:pk>/excluir/', views.atividade_delete, name='atividade_delete'),
    
    # Comunicados URLs
    path('comunicados/', views.comunicados, name='comunicados'),
    path('comunicados/novo/', views.comunicado_create, name='comunicado_create'),
    path('comunicados/<int:pk>/editar/', views.comunicado_edit, name='comunicado_edit'),
    path('comunicados/<int:pk>/excluir/', views.comunicado_delete, name='comunicado_delete'),
    
    # Perfil e Configurações URLs
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    # Outras URLs serão adicionadas aqui
] 