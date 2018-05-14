from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path

from students import views
from subjects import views as subjects_views
from tasks import views as task_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dadosAluno/$', views.show_student, name='show_student'),
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^novoAluno/$', views.create_student, name="student_new"),
    url(r'^editarAluno/(?P<pk>\d+)$', views.StudentUpdate.as_view(), name="student_edit"),
    url(r'^deletarAluno/(?P<pk>\d+)$', views.StudentDelete.as_view(), name='student_delete'),
    path('novaDisciplina/', subjects_views.create_subject, name="new_subject"),
    path('removerDisciplina/<int:pk>/', subjects_views.remove_subject_student, name="remover_disciplina"),
    path('minhasDisciplinas/', subjects_views.my_subjects, name="minhas_disciplinas"),
    path('alterarDisciplinas/<int:id>', subjects_views.update_subject, name="update_subject"),
    path('novaTarefaDisciplina/<int:subject_pk>',task_views.create_task_subject, name="new_task"),
    path('novaTarefa/',task_views.create_task_student, name="new_task_student"),
    path('minhasTarefas/', task_views.task_list, name="task_list"),
    path('editarTarefa/<int:id>', task_views.update_task, name="task_update"),
    path('apagarTarefa/<int:id>', task_views.delete_task, name="task_delete"),
]
