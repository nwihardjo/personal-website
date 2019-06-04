from __future__ import unicode_literals
from django.db import models

class Technology(models.Model):
	name = models.CharField(max_length=60)

class Project(models.Model):
	title = models.CharField(max_length=100)
	role = models.CharField(max_length=200)
	description=models.TextField(blank=True)
	image = models.FilePathField(path="/img")
	start_date = models.DateField(auto_now=True)
	end_date = models.DateField(auto_now=True)
	technology = models.ManyToManyField(Technology)
