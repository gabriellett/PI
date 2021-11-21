from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
	template=loader.get_template('bairros/index.html')
	context={}
	return HttpResponse(template.render(context,request))

def sobre_nos(request):
	return HttpResponse()
