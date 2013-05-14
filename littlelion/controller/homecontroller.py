from django.conf.urls.defaults import patterns, url
from django.http import HttpResponse
from django.shortcuts import render_to_response

def homehandler(request):
    return render_to_response('home.html')


urlpatterns = patterns('littlelion.controller.homecontroller',
            url(r'$', homehandler),
            )
