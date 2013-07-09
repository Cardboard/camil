from django.http import HttpResponse
from django.template.response import TemplateResponse
from models import Idea

def home(request):
	ideas = Idea.objects.all()
	return TemplateResponse(request, 'home.html', {'ideas': ideas})

def single_idea(request, title):
	idea = Idea.objects.get(title__exact=title)
	html = """
<html>
<head>
</head>
<body>
	<h1>{0}</h1>
	<h5>{1}</h5>
	<p>{2}</p>
	<p>{3}</p>
</body>
</html>""".format(idea.title, idea.short_desc, idea.long_desc, idea.date_formed)
	return HttpResponse(html)
