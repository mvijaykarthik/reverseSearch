from django.db import models
from django.forms import ModelForm
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms

class urlInputForm (forms.Form):
    url = forms.URLField()

