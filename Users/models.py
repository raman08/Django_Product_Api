from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	email = models.EmailField(verbose_name='email', max_length=255, unique=True)
	phone_number = models.IntegerField(verbose_name='Phone', blank=True, null=True)
	date_of_birth = models.DateField(verbose_name='DOB', blank=True, null=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

	def get_username(self) -> str:
		return self.email