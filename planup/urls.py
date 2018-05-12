from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path

from students import views
from subjects.views import list_subject, create_subject, update_subject, delete_subject

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dadosAluno/$', views.show_student, name='show_student'),
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^novoAluno/$', views.create_student, name="student_new"),
    url(r'^editarAluno/(?P<pk>\d+)$', views.StudentUpdate.as_view(), name="student_edit"),
    url(r'^deletarAluno/(?P<pk>\d+)$', views.StudentDelete.as_view(), name='student_delete'),
    path('newSubject/', create_subject, name="new_subject"),
    path('listSubject/', list_subject, name='list_subject'),
    path('updateSubject/<int:id>', update_subject, name="update_subject"),
    path('delete/<int:id>', delete_subject, name='delete_subject')
]
