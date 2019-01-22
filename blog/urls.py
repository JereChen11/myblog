from django.conf.urls import url

from blog import views

urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
	url(r'^login/$', views.login_view, name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^signup/$', views.signup_user, name='signup_user'),
	url(r'^mybloglist/$', views.mybloglist, name='mybloglist'),
	url(r'^login_error/$', views.login_error, name='login_error'),
    url(r'^error/$', views.display_error, name='error'),
    url(r'^add/$', views.add_blog, name='add_blog'),
    url(r'^(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<blog_id>[0-9]+)/delete/$', views.delete_blog, name='delete_blog'),
    url(r'^(?P<blog_id>[0-9]+)/edit/$', views.edit_blog, name='edit_blog'),
    url(r'^(?P<blog_id>[0-9]+)/(?P<blog_author>\w+)/list/$', views.jump_userbloglist, name='jump_userbloglist'),
]