from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('farms',
         views.farms, name='farms'),
    path('farm/<int:farm_id>/',
         views.farm, name='farm'),
    path('farm/<int:farm_id>/employees',
         views.farm_employees, name='farm_employees'),
    path('farm/<int:farm_id>/plants',
         views.farm_plants, name='farm_plants'),

    path('facilities',
         views.facilities, name='facilities'),
    path('facility/<int:facility_id>/',
         views.facility, name='facility'),

    path('people',
         views.people, name='people'),
    path('person/<int:person_id>/',
         views.person, name='person'),

    path('strains',
         views.strains, name='strains'),
]
