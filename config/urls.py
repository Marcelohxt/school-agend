"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # Authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),
    
    # URLs para Turmas
    path('turmas/', views.turmas, name='turmas'),
    path('turmas/nova/', views.turma_create, name='turma_create'),
    path('turmas/<int:pk>/editar/', views.turma_edit, name='turma_edit'),
    path('turmas/<int:pk>/excluir/', views.turma_delete, name='turma_delete'),
    
    # URLs para Alunos
    path('alunos/', views.alunos, name='alunos'),
    path('alunos/novo/', views.aluno_create, name='aluno_create'),
    path('alunos/<int:pk>/editar/', views.aluno_edit, name='aluno_edit'),
    path('alunos/<int:pk>/excluir/', views.aluno_delete, name='aluno_delete'),
    
    # URLs para Atividades
    path('atividades/', views.atividades, name='atividades'),
    path('atividades/nova/', views.atividade_create, name='atividade_create'),
    path('atividades/<int:pk>/editar/', views.atividade_edit, name='atividade_edit'),
    path('atividades/<int:pk>/excluir/', views.atividade_delete, name='atividade_delete'),
    
    # URLs para Comunicados
    path('comunicados/', views.comunicados, name='comunicados'),
    path('comunicados/novo/', views.comunicado_create, name='comunicado_create'),
    path('comunicados/<int:pk>/editar/', views.comunicado_edit, name='comunicado_edit'),
    path('comunicados/<int:pk>/excluir/', views.comunicado_delete, name='comunicado_delete'),

    # URLs para Professores
    path('professores/', views.professores, name='professores'),
    path('professores/novo/', views.professor_create, name='professor_create'),
    path('professores/<int:pk>/editar/', views.professor_edit, name='professor_edit'),
    path('professores/<int:pk>/excluir/', views.professor_delete, name='professor_delete'),
    
    # Outras URLs
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
