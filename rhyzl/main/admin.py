from django.contrib import admin

from .models import *

for model in (Address, Employee, Strain, Plant, Facility, Farm):
    admin.site.register(model)
