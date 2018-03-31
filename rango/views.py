# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage' : "this is my strong message"}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("This is the about page of the Rango app. \
    To go to the main page, click <a href='/rango/'>here</a>")