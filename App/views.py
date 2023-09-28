from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def  Home(req):
    return HttpResponse(loader.get_template('home.html').render())
