from django.conf.urls import url
from . import views

app_name = 'utilities'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^utility/(?P<utility_id>[0-9]+)$', views.utility_detail, name='utility_detail'),
    url(r'^users/$', views.users, name='users'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.register, name='register'),
]