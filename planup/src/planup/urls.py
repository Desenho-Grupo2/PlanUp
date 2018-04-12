from django.conf.urls import url
from django.contrib import admin

from students import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.student_list, name="student_list"),## home page
    url(r'^newStudent$', views.create_student, name="student_new"),
    url(r'^editStudent/(?P<pk>\d+)/$', views.edit_student, name="student_edit"),
    url(r'^deleteStudent/(?P<pk>\d+)$', views.delete_student, name='student_delete'),
    url(r'^showStudent/(?P<pk>\d+)$', views.show_student, name="student_show"),
]