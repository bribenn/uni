from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Raw_data(models.Model):
	address = models.CharField(max_length = 255)
	sq_ft = models.CharField(max_length = 255)
	price = models.CharField(max_length = 255)

class Destination_data(models.Model):
	address = models.CharField(max_length = 255)
	sq_ft = models.IntegerField()
	price = models.IntegerField()
	price_per_sq_ft = models.DecimalField(max_digits = 10, decimal_places = 2)