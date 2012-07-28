
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.template.loader import get_template
from django.template.context import Context, RequestContext
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from forms import *

def home(request):
    currentForm = urlInputForm
    return render_to_response('home.html',locals(), context_instance = RequestContext(request))

def processUrl(request):
    if request.method == 'POST':
        currentForm = urlInputForm(request.POST) 
        print "l1"
        if currentForm.is_valid():
            print "l2"
            url = currentForm['url'].value()
            print url
        else:
            print "l3"
            invalidUrl = True
            return render_to_response('home.html', locals(), context_instance = RequestContext(request))
    suggestions = ['123', '456']
    return render_to_response('suggestions.html', locals(), context_instance = RequestContext(request))

