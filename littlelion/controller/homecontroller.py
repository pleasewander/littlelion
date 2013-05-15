from django.conf.urls.defaults import patterns, url
from django.http import HttpResponse
from django.shortcuts import render

def homehandler(request):
    return render(request,'home.html')


urlpatterns = patterns('littlelion.controller.homecontroller',
            url(r'$', homehandler),
            )
