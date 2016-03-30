from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import Http404                                                 
from django.template import RequestContext, loader

import django_tables2

import itservices.models                                                                              
import itservices.tables

import pdb

# from .forms import ITServicesForm, GroupsForm

def itservices_list(request):
    table = itservices.tables.ITServicesTable(itservices.models.ITService.objects.all())
    django_tables2.RequestConfig(request, paginate=False).configure(table)
    
    return render(request, 'itservices/itservices_list.html', {'table': table})

def groups_list(request):
    table = itservices.tables.GroupsTable(itservices.models.Group.objects.all())
    django_tables2.RequestConfig(request, paginate=False).configure(table)

    return render(request, 'itservices/groups_list.html', {'table': table})


