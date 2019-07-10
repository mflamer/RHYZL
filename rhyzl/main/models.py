from django.db.models import *
from django.contrib.auth.models import User

class Address(Model):
    number = PositiveIntegerField()
    street = CharField(max_length=32)
    city = CharField(max_length=32)
    state = CharField(max_length=32)
    zip = PositiveIntegerField()
    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.street,
                                           self.number,
                                           self.city,
                                           self.state,
                                           self.zip)

class Person(Model):
    user_name = CharField(max_length=32)
    name_first = CharField(max_length=32)
    name_last = CharField(max_length=32)
    email = EmailField()
    address = ForeignKey(Address, on_delete=CASCADE)

    def __str__(self):
        return '{} {} ({})'.format(self.name_first,
                                   self.name_last,
                                   self.user_name)
class Employee(Person):
    hire_date = DateField()
    pay_rate = DecimalField(max_digits=5, decimal_places=2)

class Strain(Model):
    metrc_Id = PositiveIntegerField()
    name = CharField(max_length=32)
    thc_level = DecimalField(max_digits=4, decimal_places=4)
    cbd_level = DecimalField(max_digits=4, decimal_places=4)
    def __str__(self):
        return self.name

class Plant(Model):
    strain = ForeignKey(Strain, on_delete=CASCADE)
    date_planted = DateField()
    date_harvested = DateField()
    weight_harvested = DecimalField(max_digits=5, decimal_places=2)
    tag = CharField(max_length=32)
    def __str__(self):
        return '{} {}'.format(self.strain, self.tag)

class Facility(Model):
    name = CharField(max_length=32)
    address = ForeignKey(Address, on_delete=CASCADE)

    def __str__(self):
        return self.name

class Farm(Facility):
    plants = ManyToManyField(Plant, blank=True)
