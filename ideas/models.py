import datetime
from django.db import models
from django.forms import ModelForm, Textarea
from django import forms

class Link(models.Model):
    url = models.URLField()

class Tag(models.Model):
    tag = models.CharField(max_length=16)

class Source(models.Model):
    source = models.CharField(max_length=160)

class Image(models.Model):
    url = models.URLField()

class Idea(models.Model):
    title = models.CharField(max_length=32, unique=True)
    CHOICES = (('idea', 'idea'),
		('wip', 'wip'),
		('finished', 'finished'))
    status = models.CharField(max_length=8, choices=CHOICES)
    short_desc = models.CharField(max_length=128)
    long_desc = models.TextField()
    links = models.ManyToManyField(Link, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    sources = models.ManyToManyField(Source, blank=True)
    images = models.ManyToManyField(Image, blank=True)
    date_formed = models.DateField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.title

    def title_nospaces(self):
	return self.title.replace(' ', '_')

    def are_links(self):
	if self.links.all().values()[0]['url'] != u'':
	    return True 

    def are_tags(self):
	if self.tags.all().values()[0]['tag'] != u'':
	    return True

    def are_sources(self):
	if self.sources.all().values()[0]['source'] != u'':
	    return True

    def are_images(self):
	if self.images.all().values()[0]['url'] != u'':
	    return True

class IdeaForm(forms.Form):
    title = forms.CharField(max_length=32)
    CHOICES = (('idea', 'idea'),
		('wip', 'wip'),
		('finished', 'finished'))
    status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    short_desc = forms.CharField(max_length=128)
    long_desc = forms.CharField(widget=forms.Textarea())
    #long_desc = forms.Textarea()
    links = forms.CharField(required=False)
    tags = forms.CharField(required=False)
    sources = forms.CharField(required=False)
    images = forms.CharField(required=False)
    date_formed = forms.DateField(
	widget=forms.widgets.DateInput(format="%m/%d/%Y"),
                                    initial=datetime.datetime.now)

#    def clean_title(self):
#	cleaned_title = self.cleaned_data
#	try:
#	    title = cleaned_title['title']
#	    try:
#		idea = Idea.objects.get(title__exact=title)
#	    except:
#		idea = False
#	    if title and idea:
#		raise forms.ValidationError("Title must be unique")
#	except KeyError:
#	    pass 
#	return cleaned_title

    def clean(self):
	cleaned_data = self.cleaned_data
	print('IdeaForm.clean()')
	try:
	    title = cleaned_data['title'] 
	    try:
                # see if the idea with the entered title already exists
		idea = Idea.objects.get(title__exact=title)
	    except:
		idea = False
	    if title and idea: # idea already exists
		raise forms.ValidationError("Title must be unique")
	except KeyError:
	    pass 
	return cleaned_data

#class IdeaForm(ModelForm):
#    class Meta:
#	model = Idea
#	fields = ['title', 'short_desc', 'long_desc', 'links', 'tags', 'sources', 'images', 'date_formed']
#	widgets = {
#		'links': CommaTextInput(),
#		'date_formed': forms.widgets.DateInput(format='%m/%d/%Y')}

	
