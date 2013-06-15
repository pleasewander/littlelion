from django.contrib.auth.models import User
from django.contrib import auth
from django.conf.urls.defaults import patterns, url
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
import json

def createaccountpage(request):
    return render(request, 'register.html')

def register(request):
    firstName =  request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    email = request.POST.get('email')
    password = request.POST.get('password')

    success = False

    if checkEmailExists(email) == False:
        success = True
        user = User.objects.create_user(username=email, first_name=firstName, last_name=lastName, email=email)

    response = HttpResponse()
    response['content-type'] = 'application/json'
    response.write(json.dumps({'success': success}))
    return response

def dologin(request):
    userEmail = request.POST.get('email')
    userPassword = request.POST.get('password')

    user = auth.authenticate(username=userEmail, password=userPassword)
    success = True
    msg = ''

    if user is not None:
        auth.login(request, user)
        success = True
    else:
        success = False
        msg = 'Not a valid account'

    response = HttpResponse()
    response['content-type'] = 'application/json'
    response.write(json.dumps({'success' : success , 'message' : msg }))

    return response

def dologout(request):
    auth.logout(request)
    return render(request, 'home.html')


def checkEmail(request):
    email = request.POST.get('email')
    status = True
    if checkEmailExists(email):
        status = False

    response = HttpResponse()
    response['Content-Type'] = 'application/json'
    response.write(json.dumps({'success' : status}))
    return response

def checkEmailExists(emailToCheck):
    status = True
    numberOfUsers = User.objects.all().filter(email= emailToCheck).count()

    if numberOfUsers == 0 :
        status = False

    if emailToCheck == '':
        status = False

    return status

urlpatterns = patterns('littlelion.controller.accountcontroller',
            url(r'^register$', createaccountpage),
            url(r'^createaccount$', register),
            url(r'^login', dologin),
            url(r'^logout', dologout),
            url(r'^checkemail', checkEmail)
            )