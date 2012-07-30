from django.db import models
#from django import forms
from django import newforms as forms
class urlInputForm (forms.Form):
    url = forms.URLField()

