from django.db import models

class File(models.Model):
	name 				= models.CharField(max_length=50, null=False, blank=True)
	one_file 			= models.FileField(upload_to="files", null=False, blank=True)

	def __str__(self):
		return self.name