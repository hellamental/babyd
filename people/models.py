from django.db import models


RELATIONSHIP_CHOICES = (
		('Mother', 'Mother'),
		('Father', 'Father'),
		('Aunty', 'Aunty'),
		('Uncle', 'Uncle'),
		('Cousin', 'Cousin'),
		('Grandmother','Grandmother'),
		('Grandfather','Grandfather'),
		('2nd Cousin', '2nd Cousin'),
	)

class People(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	relationship = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES)

	def __str__(self):
		return self.first_name


class Media(models.Model):
	person = models.ForeignKey(People, on_delete=models.CASCADE)
	file_name = models.CharField(max_length=50)
	uploaded_file = models.FileField(upload_to='uploads/')
	uploaded_image = models.ImageField(default=None, upload_to='img/')

	def __str__(self):
		return self.file_name


