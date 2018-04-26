from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin

from students import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dadosAluno/$', views.show_student, name='show_student'),
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^novoAluno/$', views.create_student, name="student_new"),
    url(r'^editarAluno/(?P<pk>\d+)$', views.StudentUpdate.as_view(), name="student_edit"),
    url(r'^deletarAluno/(?P<pk>\d+)$', views.StudentDelete.as_view(), name='student_delete'),
]