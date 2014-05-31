from django.conf.urls import include, patterns, url

urlpatterns = patterns('',
	url(r'^new/$', 'ideas.views.new_idea'),
	url(r'^idea/(?P<title_nospaces>\w+)/$', 'ideas.views.single_idea'),
	url(r'^edit/(?P<title_nospaces>\w+)/$', 'ideas.views.edit_idea'),
	url(r'^delete/(?P<title_nospaces>\w+)/$', 'ideas.views.delete_idea'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'ideas.views.logout_view'),
	url(r'^$', 'ideas.views.home'),

)
