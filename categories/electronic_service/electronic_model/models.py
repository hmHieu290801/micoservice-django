# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# This is our model for user registration.
class electronic(models.Model):

	### followings are the fields of our table.
	electronic_id = models.CharField(max_length=10)
	name = models.CharField(max_length=50)
	price = models.CharField(max_length=10)
	description = models.CharField(max_length=20)

	### It will help to print the values.
	def __str__(self):
		return '%s %s %s %s %s ' % (self.electronic_id, self.name, self.price, self.description)