# -*- coding: utf-8 -*-

# imports
from __future__ import unicode_literals
from django.shortcuts import render

# views
def index(request):
    return render(request, "index.html")
