from . import views
from django.conf.urls import url 
from django.urls import path

urlpatterns = [
	# /bairros/
    url('^$', views.index, name='index'),

    # /sobre_nos/
    url('sobre_nos', views.sobre_nos, name='sobre_nos')
]
