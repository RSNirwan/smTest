# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.conf import settings 
import json
from .forms import UserForm
from .models import User



def get_available_widget_names():
	path = settings.BASE_DIR + '/static/other/default.json'
	obj =  json.loads(open(path).read())
	return obj.keys()

def home(request, name=None):
	title = "My Title"
	
	form = UserForm(request.POST or None)
	content = {
		"title": title, 
		"form": form,
		"name": name
	}

	if form.is_valid():
		form.save(commit=True)
		content['thanks'] = 'Welcome {}!'.format(form.cleaned_data['user_name'])

	queryset = User.objects.all().order_by('-updated')
	widget_list = get_available_widget_names()
	content['queryset'] = queryset
	content['widget_list'] = widget_list
	content['widget_list_as_string'] = json.dumps(widget_list)

	#render users config if exists
	content['config'] = ''
	if name is not None:
		#config = queryset.filter(user_name=name)[0].user_config
		content['config'] = queryset.filter(user_name=name)[0].user_config

	return render(request, "home.html", content)


def get_user_config(request):
	name = request.POST.get("name")
	conf = request.POST.get("users_widgets")
	instance = User.objects.get(user_name=name)
	instance.user_config = conf
	instance.save()
	return render(request, 'test.html', {})