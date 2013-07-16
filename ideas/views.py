from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render
from models import Idea, IdeaForm, Link, Tag, Source, Image

def home(request):
	ideas = Idea.objects.all()
	return TemplateResponse(request, 'home.html', {'ideas': ideas})

def single_idea(request, title):
	title_nospaces = title.replace('_', ' ')
	idea = Idea.objects.get(title__exact=title_nospaces)
	return TemplateResponse(request, 'idea.html', {'idea': idea})

def new_idea(request):
    if request.method == 'POST': #if form has been submitted
	form = IdeaForm(request.POST) # a form bound to the post data
	if form.is_valid(): # all validation rules pass
	    # process data in form.cleaned_data
	    title = form.cleaned_data['title']
	    title_nospaces = str(title.replace(' ', '_').lower())
	    short_desc = form.cleaned_data['short_desc']
	    long_desc = form.cleaned_data['long_desc']
	    date_formed = form.cleaned_data['date_formed']
	    links_strings = form.cleaned_data['links'].split(',')
	    tags_strings = form.cleaned_data['tags'].split(',')
	    sources_strings = form.cleaned_data['sources'].split(',')
	    images_strings = form.cleaned_data['images'].split(',')
	    # save new idea with cleaned form data
	    new_idea = Idea(title=title,short_desc=short_desc,long_desc=long_desc,date_formed=date_formed)
	    new_idea.save()
	    # add links, tags, sources, and images
	    for link in links_strings:
		new_link = Link(url=link)
		new_link.save()
		new_idea.links.add(new_link)
	    for tag in tags_strings:
		new_tag = Tag(tag=tag)
		new_tag.save()
		new_idea.tags.add(new_tag)
	    for source in sources_strings:
		new_source = Source(source=source)
		new_source.save()
		new_idea.sources.add(new_source)
	    for image in images_strings:
		new_image = Image(url=image)
		new_image.save()
		new_idea.images.add(new_image)
	    # save after adding data
	    new_idea.save()
	    
	    return HttpResponseRedirect('/idea/' + title_nospaces + '/')
    else:
	form = IdeaForm() # unbound form

    return render(request, 'new_idea.html', {
	'form': form,
	})
