from django.conf import settings
from django.utils import timezone
from django.db import models

PERSON_CHOICES = (
    ('one', 'One'),
    ('two', 'Two'),
    ('three', 'Three'),
    ('four', 'Four')
)

AREA_CHOICES = (
    ('marathahalli', 'marathahalli'),
    ('HSR Layout', 'HSR Layout'),
    ('mg road', 'mg Road'),
    ('BTM layout', 'BTM layout'),
    ('Basavangudi', 'Basavangudi'),
)

PG_TYPE_CHOICES = (
    ('1*', '1*'),
    ('2*', '2*'),
    ('3*', '3*'),
    ('4*', '4*')
)

class FacilitiesPrice(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    fname = models.CharField(max_length=30, verbose_name='First Name')
    lname = models.CharField(max_length=30, verbose_name='Last Name')
    pg_type = models.CharField(max_length=5, choices=PG_TYPE_CHOICES)
    no_of_person = models.CharField(max_length=5, choices=PERSON_CHOICES, default='one')
    wifi = models.BooleanField( null=True)
    laundry = models.BooleanField( null=True)
    food = models.BooleanField( null=True)
    maid = models.BooleanField( null=True)
    arrival_date = models.DateField(default=timezone.now)
    departure_date = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=10)
    sharing = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    
    def __str__(self):
        return self.fname

class ContactUs(models.Model):
    fname = models.CharField(max_length=30, verbose_name='First Name')
    lname = models.CharField(max_length=30, verbose_name='Last Name')
    email = models.EmailField(null=True)
    contact = models.BigIntegerField(default=0)
    message = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.fname

class Review(models.Model):
    fname = models.CharField(max_length=30, verbose_name='First Name')
    lname = models.CharField(max_length=30, verbose_name='Last Name')
    email = models.EmailField(null=True)
    pg_type = models.CharField(max_length=5, choices=PG_TYPE_CHOICES, verbose_name='PG Type')
    comfort = models.CharField(max_length=20)
    cost = models.CharField(max_length=20)
    quality = models.CharField(max_length=20)

    def __str__(self):
        return self.fname

class CheckAvailability(models.Model):
    name = models.CharField(max_length=30)
    pg_type = models.CharField(max_length=5, choices=PG_TYPE_CHOICES, verbose_name='PG Type')
    available_from = models.DateField(default=timezone.now)
    available_to = models.DateField(default=timezone.now)
    no_of_person = models.CharField(max_length=5, choices=PERSON_CHOICES, default='one')
    email = models.EmailField(null=True)
    area = models.CharField(max_length=20, choices=AREA_CHOICES)
    available = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=30, unique=True)
    contact = models.BigIntegerField(default=0)
    email = models.EmailField(null=True)
    pg_type = models.CharField(max_length=5, choices=PG_TYPE_CHOICES, verbose_name='PG Type')
    description = models.TextField(max_length=200, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    sharing = models.CharField(max_length=20)
    wifi = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    maid = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product_images', blank=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    photo = models.ForeignKey(Owner, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images', blank=True)

    def __str__(self):
        return self.photo.name

class Payment(models.Model):
    ac_no = models.BigIntegerField(default=0, verbose_name='A/C No')
    ini_balance = models.IntegerField(default=0, verbose_name='Initial Balance')
    rem_balance = models.IntegerField(default=0, verbose_name='Remaining Balance')

    def __str__(self):
        return str(self.ac_no)
