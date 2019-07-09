from django.db.models import *
from django.contrib.auth.models import User

class Address(Model):
    number = PositiveIntegerField()
    street = CharField(max_length=32)
    city = CharField(max_length=32)
    state = CharField(max_length=32)
    zip = PositiveIntegerField()

class Person(Model):
    name_first = CharField(max_length=32)
    name_last = CharField(max_length=32)
    email = EmailField()
    address = ForeignKey(Address, on_delete=CASCADE)    

class Employee(Person):
    hire_date = DateField()
    pay_rate = DecimalField(max_digits=5, decimal_places=2)

class Strain(Model):
    metrc_Id = PositiveIntegerField()
    name = CharField(max_length=32)
    thc_level = DecimalField(max_digits=4, decimal_places=4)
    cbd_level = DecimalField(max_digits=4, decimal_places=4)
    
class Plant(Model):
    strain = ForeignKey(Strain, on_delete=CASCADE)      
    date_planted = DateField()
    date_harvested = DateField()
    weight_harvested = DecimalField(max_digits=5, decimal_places=2)
    tag = CharField(max_length=32)

class Facility(Model):
    name = CharField(max_length=32)
    address = ForeignKey(Address, on_delete=CASCADE)        

class Farm(Facility):   
    plants = ManyToManyField(Plant, blank=True) 

    