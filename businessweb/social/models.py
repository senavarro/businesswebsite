from django.db import models

# Create your models here.
class Link(models.Model):
	key=models.SlugField(verbose_name="Key Name", max_length=100, unique=True)
	name=models.CharField(verbose_name="Social Network", max_length=200)
	url= models.URLField(verbose_name="Link", max_length=200, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "link"
		verbose_name_plural = "links"
		ordering = ["name"]

	def __str__(self):
		return self.name
