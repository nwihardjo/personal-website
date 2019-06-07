from __future__ import unicode_literals
from django.db import models

class Technology(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Project(models.Model):
	title = models.CharField(max_length=100)
	role = models.CharField(max_length=200)
	description=models.TextField(blank=True)
	image = models.FilePathField(path="/img")
	start_date = models.DateField(auto_now=False)
	end_date = models.DateField(auto_now=False)
	technology = models.ManyToManyField(Technology)
	url = models.URLField(max_length=200, blank=True)

	class Meta:
		ordering = ['-end_date__year', '-end_date__month']

	def __str__(self):
		return self.title
