from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path

from students import views
from subjects.views import list_subject, create_subject, update_subject, delete_subject, add_subject_student,remove_subject_student,my_subjects

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dadosAluno/$', views.show_student, name='show_student'),
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^novoAluno/$', views.create_student, name="student_new"),
    url(r'^editarAluno/(?P<pk>\d+)$', views.StudentUpdate.as_view(), name="student_edit"),
    url(r'^deletarAluno/(?P<pk>\d+)$', views.StudentDelete.as_view(), name='student_delete'),
    path('novaDisciplina/', create_subject, name="new_subject"),
    path('listaDeDisciplinas/', list_subject, name='list_subject'),
    path('adicionarDisciplina/<int:pk>/', add_subject_student, name="adicionar_disciplina"),
    path('removerDisciplina/<int:pk>/', remove_subject_student, name="remover_disciplina"),
    path('minhasMaterias/', my_subjects, name="minhas_disciplinas"),
    path('alterarDisciplinas/<int:id>', update_subject, name="update_subject"),
    path('excluirDisciplinas/<int:id>', delete_subject, name='delete_subject')
]
