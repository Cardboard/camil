from django.db import models

class Link(models.Model):
	url = models.URLField()
	def __unicode__(self):
		return self.name

class Tag(models.Model):
	tag = models.CharField(max_length=16)
	def __unicode__(self):
		return self.name

class Source(models.Model):
	source = models.CharField(max_length=160)
	def __unicode__(self):
		return self.name

class Image(models.Model):
	url = models.URLField()
	def __unicode__(self):
		return self.name

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
