from io import BytesIO

from django.db import models
from django.core.files import File

from PIL import Image

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField()

	class Meta:
		ordering = ('name',)

	def __str__(self) -> str:
		return self.name

	def get_absolute_url(self):
		return f'/{self.slug}/'


class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	slug = models.SlugField()
	description =models.TextField(blank=True, null=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.ImageField(upload_to='uploads/', blank=True, null=True)
	thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-date_added',)

	def __str__(self) -> str:
		return self.name

	def get_absolute_url(self):
		return f'/{self.category.slug}/{self.slug}/'

	def get_image(self):
		if self.image:
			return f'http://localhost:8000/{self.image}'
		return ''

	def get_thumbnail(self):
		if self.thumbnail:
			return f'http://localhost:8000/{self.thumbnail}'
		else:
			if self.image:
				self.thumbnail = self.make_thumbmail(self.image)
				self.save()

				return f'http://localhost:8000/{self.thumbnail}'
			else:
				return ''

	def make_thumbnail(self, image, size=(300,200)):
		img = Image.open(image)
		img.convert('rgb')
		img.thumbnail(size)

		thumb_io = BytesIO()
		img.save(thumb_io, 'jpeg', quality=85)

		thumbnail = File(thumb_io, name=image.name)

		return thumbnail