
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.template.loader import get_template
from django.template.context import Context, RequestContext
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from forms import *
from google.appengine.api.urlfetch import *
import html2text
def home(request):
    currentForm = urlInputForm()
    return render_to_response('home.html',locals(), context_instance = RequestContext(request))

def fixEncoding(text):
    op = ""
    for i in range(0, len(text)):
        if ord(text[i]) < 128:
            op += text[i]
    return op
def processUrl(request):
    if request.method == 'POST':
        currentForm = urlInputForm(request.POST) 
        if currentForm.is_valid():
            urlToFetch =  currentForm.clean_data['url']
            #urlToFetch = currentForm.cleaned_data['url']
            #print urlToFetch 
            html = fetch(url = urlToFetch).content
            html = fixEncoding(html)
            print "Extracted Data <br/>"
            text = html2text.html2text(html)
            text = text.replace("\n", "<br/>")
            print fixEncoding(text)
            print "<br/>"
        else:
            return render_to_response('home.html', locals(), context_instance = RequestContext(request))
    suggestions = ['123', '456']
    return render_to_response('suggestions.html', locals(), context_instance = RequestContext(request))

