from django.conf.urls import include, patterns, url

urlpatterns = patterns('',
	url(r'^new/$', 'ideas.views.new_idea'),
	url(r'^idea/(?P<title>\w+)/$', 'ideas.views.single_idea'),
	url(r'^$', 'ideas.views.home'),

)
