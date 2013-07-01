from django.conf.urls import include, patterns, url

urlpatterns = patterns('',
	url(r'^idea/(?P<title>\w+)/$', 'ideas.views.single_idea'),
	url(r'^$', 'ideas.views.home'),

)
