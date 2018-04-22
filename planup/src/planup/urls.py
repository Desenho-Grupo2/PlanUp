from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin

from students import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.student_list, name="student_list"),## home page
    #url(r'^newStudent$', views.create_student, name="student_new"),
    #url(r'^editStudent/(?P<pk>\d+)/$', views.edit_student, name="student_edit"),
    #url(r'^deleteStudent/(?P<pk>\d+)$', views.delete_student, name='student_delete'),
    #url(r'^showStudent/(?P<pk>\d+)$', views.show_student, name="student_show"),

    url(r'^dadosAluno/$', views.show_student, name='show_student'),
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^novoAluno/$', views.create_student, name="student_new"),
    url(r'^editarAluno/$', views.edit_student, name="student_edit"),
]