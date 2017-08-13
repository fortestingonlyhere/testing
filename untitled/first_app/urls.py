from django.conf.urls import url
from first_app import views

#template tagging
app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.indexx, name='indexx'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^relative/$',views.relative, name='relative'),
    url(r'^other/$',views.other, name='other'),
]

