from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('farms',
         views.farms, name='farms'),
    path('farm/<str:name>/',
         views.farm, name='farm'),
    path('farm/<str:name>/employees',
         views.farm_employees, name='farm_employees'),
    path('farm/<str:name>/plants',
         views.farm_plants, name='farm_plants'),

    path('facilities',
         views.facilities, name='facilities'),
    path('facility/<str:name>/',
         views.facility, name='facility'),

    path('people',
         views.people, name='people'),
    path('person/<str:user_name>/',
         views.person, name='person'),

    path('strains',
         views.strains, name='strains'),
]
