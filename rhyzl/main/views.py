from django.shortcuts import render

from django.http import HttpResponse

from .models import Farm

def index(request):
    return HttpResponse('INDEX STUB')

def farms(request):
    # List of all farms
    farm_list = Farm.objects.order_by('name')
    context = {'farm_list': farm_list}
    return render(request, 'main/farms.html', context)

def farm(request, name):
    # Info about farm NAME
    return HttpResponse('FARM ' + name)

def farm_employees(request, name):
    # Employees at farm NAME
    return HttpResponse('FARM EMPLOYEES' + name)

def farm_plants(request, name):
    # Plants belonging to farm NAME
    return HttpResponse('FARM PLANTS' + name)

def facilities(request):
    # List of all facilities
    return HttpResponse('FACILITIES')

def facility(request, name):
    # Info about facility NAME
    return HttpResponse('NAME ' + str(name))

def people(request):
    # List of all people
    return HttpResponse('PEOPLE')

def person(request, user_name):
    # Info about person with USER_NAME
    return HttpResponse('USER_NAME ' + user_name)

def strains(request):
    # List of all known strains
    return HttpResponse('STRAINS')

def strain(request, metric_id):
    # Info about strain with STRAIN_ID
    return HttpResponse('STRAIN_ID ' + str(metric_id))
