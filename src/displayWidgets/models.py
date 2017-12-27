# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings 

#
import json

def initial_config():
	path = settings.BASE_DIR + '/static/other/initial_config.json'
	return open(path).read()



class User(models.Model):
	user_name = models.CharField(max_length=50)
	user_config = models.TextField(max_length=5000, default=initial_config)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.user_name

