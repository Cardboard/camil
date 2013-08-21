from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render
from models import Idea, IdeaForm, Link, Tag, Source, Image

def home(request):
    ideas = Idea.objects.all()
    return TemplateResponse(request, 'home.html', {'ideas': ideas})

def single_idea(request, title_nospaces):
    title_withspaces = title_nospaces.replace('_', ' ')
    idea = Idea.objects.get(title__exact=title_withspaces)
    return TemplateResponse(request, 'idea.html', {'idea': idea})

def edit_idea(request, title_nospaces):
    if request.method == 'POST': # if form has been submitted
	form = IdeaForm(request.POST) # a form bound to the post data

	# delete old idea before saving so we don't end up
	# with two objects with the same title
	title_withspaces = title_nospaces.replace('_', ' ')
	old_idea = Idea.objects.get(title__exact=title_withspaces)
	old_idea.delete()
	print('Idea \'{}\' deleted!'.format(title_withspaces))

	if form.is_valid(): # all validation rules pass
	    print('Form is valid')
	    title = save_idea(form)
	    return HttpResponseRedirect('/ideas/idea/' + title.replace(' ','_') + '/')
    else:
	form = IdeaForm() # unbound form

	title_withspaces = title_nospaces.replace('_', ' ')
	idea = Idea.objects.get(title__exact=title_withspaces)
	# fill out form with the data from the object
	# ripe for the editing!
	form = IdeaForm(initial={
			'title': idea.title,
			'status': idea.status,
			'short_desc': idea.short_desc,
			'long_desc': idea.long_desc,
			'links': get_field_string(idea.links),
			'tags': get_field_string(idea.tags),
			'sources': get_field_string(idea.sources),
			'images': get_field_string(idea.images),
			'date_formed': idea.date_formed})
    return render(request, 'new_idea.html', {
	'form': form,
	'idea': idea,
	'edit': True
	})

def new_idea(request):
    if request.method == 'POST': #if form has been submitted
	form = IdeaForm(request.POST) # a form bound to the post data
	if form.is_valid(): # all validation rules pass
	    title = save_idea(form)
	    return HttpResponseRedirect('/ideas/idea/' + title.replace(' ','_') + '/')
    else:
	form = IdeaForm(initial={'status': 'idea'}) # unbound form

    return render(request, 'new_idea.html', {
	'form': form,
	'idea': None,
	'edit': False
	})

def get_field_string(infield):
    outfield = ''
    # add each url, link, etc. to a comma-delimited string
    for item in infield.values_list():
	if item[1] != u'':
	    outfield += item[1]
	    outfield += ','
    # remove trailing comma
    if outfield.endswith(','):
	outfield = outfield[:-1]
    # return created string 
    return outfield # fly ball!

def save_idea(form):
    # process data in form.cleaned_data
    title = form.cleaned_data['title']
    title_nospaces = str(title.replace(' ', '_').lower())
    status = form.cleaned_data['status']
    short_desc = form.cleaned_data['short_desc']
    long_desc = form.cleaned_data['long_desc']
    date_formed = form.cleaned_data['date_formed']
    links_strings = form.cleaned_data['links'].split(',')
    tags_strings = form.cleaned_data['tags'].split(',')
    sources_strings = form.cleaned_data['sources'].split(',')
    images_strings = form.cleaned_data['images'].split(',')
    # save new idea with cleaned form data
    new_idea = Idea(title=title,status=status,short_desc=short_desc,
		    long_desc=long_desc,date_formed=date_formed)
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
    return title
    
def delete_idea(request, title_nospaces):
    # get the idea and delete it
    title_withspaces = title_nospaces.replace('_',' ')
    idea = Idea.objects.get(title__exact=title_withspaces)
    idea.delete()
    # get all ideas to populate the master list with
    ideas = Idea.objects.all()
    return HttpResponseRedirect('/ideas')
