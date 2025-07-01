from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	name = models.CharField(max_length=120)
	logo = models.ImageField(upload_to='customers', default='no-image.png')

	def __str__(self):
		return str(self.name)


class Product(models.Model):
	name = models.CharField(max_length=120)
	image = models.ImageField(upload_to='products', default='no-image.png')
	price = models.FloatField(help_text='In USD $')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.name} - {self.created.strftime('%d/%m/%Y')}"


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(default='No bio')
	avatar = models.ImageField(upload_to='avatars', default='no-image.png')

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"Profile of {self.user.username}"
