from django.conf.urls import url
from . import views

app_name = 'utilities'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.register_user, name='register_user'),

    url(r'^utility/utility_sort/$', views.utility_sort, name='utility_sort'),
    url(r'^utility/(?P<utility_id>[0-9]+)/$', views.utility_detail, name='utility_detail'),

    url(r'^users/$', views.users, name='users'),
    url(r'^users/username_sort$', views.username_sort, name='username_sort'),
    url(r'^users/login_sort$', views.login_sort, name='login_sort'),
    url(r'^users/joined_sort$', views.joined_sort, name='joined_sort'),

    url(r'^user/(?P<user_id>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^user/(?P<user_id>[0-9]+)/remove/$', views.remove_user, name='remove_user'),
    url(r'^user/(?P<user_id>[0-9]+)/disable/$', views.disable_user, name='disable_user'),
    url(r'^user/(?P<user_id>[0-9]+)/enable/$', views.enable_user, name='enable_user'),
    url(r'^user/(?P<user_id>[0-9]+)/set_manager/$', views.set_manager, name='set_manager'),
    url(r'^user/(?P<user_id>[0-9]+)/add_utility/$', views.add_utility, name='add_utility'),
    url(r'^user/(?P<user_id>[0-9]+)/add_utility/(?P<utility_id>[0-9]+)/$', views.adding_util, name='adding_util'),
    url(r'^user/(?P<user_id>[0-9]+)/remove_utility/(?P<utility_id>[0-9]+)/$', views.remove_utility, name='remove_utility'),
]