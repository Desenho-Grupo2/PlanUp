from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from students import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.StudentList.as_view(), name="student_list"),## home page
    url(r'^newStudent$', views.StudentCreate.as_view(), name="student_new"),
    url(r'^editStudent/(?P<pk>\d+)$', views.StudentUpdate.as_view(), name="student_edit"),
    url(r'^deleteStudent/(?P<pk>\d+)$', views.StudentDelete.as_view(), name='student_delete'),
    url(r'^showStudent/(?P<pk>\d+)$', views.StudentShow.as_view(), name="student_show"),
    #login 
     url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),


]