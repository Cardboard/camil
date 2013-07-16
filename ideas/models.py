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
    title = models.CharField(max_length=32)
    short_desc = models.CharField(max_length=128)
    long_desc = models.CharField(max_length=255)
    links = models.ManyToManyField(Link, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    sources = models.ManyToManyField(Source, blank=True)
    images = models.ManyToManyField(Image, blank=True)
    date_formed = models.DateField()

    def __unicode__(self):
	    return self.title

class IdeaForm(forms.Form):
    title = forms.CharField(max_length=32)
    short_desc = forms.CharField(max_length=128)
    long_desc = forms.CharField(max_length=255)
    links = forms.CharField(required=False)
    tags = forms.CharField(required=False)
    sources = forms.CharField(required=False)
    images = forms.CharField(required=False)
    date_formed = forms.DateField(
	widget=forms.widgets.DateInput(format="%m/%d/%Y"))

#class IdeaForm(ModelForm):
#    class Meta:
#	model = Idea
#	fields = ['title', 'short_desc', 'long_desc', 'links', 'tags', 'sources', 'images', 'date_formed']
#	widgets = {
#		'links': CommaTextInput(),
#		'date_formed': forms.widgets.DateInput(format='%m/%d/%Y')}

	
