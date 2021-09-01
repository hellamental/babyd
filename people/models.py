from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

RELATIONSHIP_CHOICES = (
		('Immediate', 'Immediate'),
		('Distant', 'Distant'),
		('Friend', 'Friend'),
	)

class People(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	relationship = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES)

	def __str__(self):
		return self.first_name


class Media(models.Model):
	person = models.ForeignKey(People, on_delete=models.CASCADE)
	uploaded_file = models.FileField(default=None,upload_to='uploads/')
	file_name = models.CharField(default=None,max_length=50)
	file_information = models.TextField(default=None,max_length=100)

	def __str__(self):
		return self.file_name

class Images(models.Model):
	person = models.ForeignKey(People, on_delete=models.CASCADE)
	uploaded_image = models.ImageField(default=None, upload_to='img/')
	image_title = models.CharField(default=None,max_length=50)
	image_caption = models.CharField(default=None,max_length=100)
	
	def __str__(self):
		return self.image_title