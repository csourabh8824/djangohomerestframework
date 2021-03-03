from django.db import models

class Product(models.Model):
	title = models.CharField(max_length=200)
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the Product')