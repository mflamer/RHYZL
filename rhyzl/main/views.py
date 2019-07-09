from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('INDEX STUB')

def farms(request):
    # List of all farms
    return HttpResponse('FARMS')

def farm(request, farm_id):
    # Info about farm with FARM_ID
    return HttpResponse('FARM ' + str(farm_id))

def farm_employees(request, farm_id):
    # Employees at a farm with FARM_ID
    return HttpResponse('FARM EMPLOYEES' + str(farm_id))

def farm_plants(request, farm_id):
    # Plants belonging to a FARM_ID
    return HttpResponse('FARM PLANTS' + str(farm_id))

def facilities(request):
    # List of all facilities
    return HttpResponse('FACILITIES')

def facility(request, facility_id):
    # Info about facility with FACILITY_ID
    return HttpResponse('FACILITY_ID ' + str(facility_id))

def people(request):
    # List of all people
    return HttpResponse('PEOPLE')

def person(request, person_id):
    # Info about person with PERSON_ID
    return HttpResponse('PERSON_ID ' + str(person_id))

def strains(request):
    # List of all known strains
    return HttpResponse('STRAINS')

def strain(request, strain_id):
    # Info about strain with STRAIN_ID
    return HttpResponse('STRAIN_ID ' + str(strain_id))
