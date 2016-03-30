from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import Http404                                                 
from django.template import RequestContext, loader

import django_tables2

import itservices.systems.models                                                                              
import itservices.systems.tables

import pdb

# from .forms import ITServicesForm, GroupsForm

def importsystems_list(request):
    table = itservices.systems.tables.ImportSystemsTable(itservices.systems.models.ImportSystems.objects.all())
    django_tables2.RequestConfig(request, paginate=False).configure(table)
    
    return render(request, 'itservices/systems/importsystems_list.html', {'table': table})

