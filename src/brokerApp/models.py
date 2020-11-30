from django.db import models

# Create your models here.
class Property(models.Model):
    TYPE_OF_PLACE = [
        ('Apartment', 'Apartment'),
        ('Townhouse', 'Townhouse'),
        ('Whole bulding', 'Whole bulding'),
        ('Loft', 'Loft'),
    ]
    ROOMS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4+'),
    ] 
    FURNISHED = [
        ('furnished','furnished'),
        ('unfurnished','unfurnished')
    ]
    RENTED= [
        ('yes','yes'),
        ('no','no'),
        ('ending','ending')
    ]
    renting     = models.CharField(max_length=10, choices=RENTED, null=True, blank=True)
    about       = models.TextField(max_length=355, null=True, blank=True)
    place_type  = models.CharField(max_length=20, choices=TYPE_OF_PLACE)
    furniture   = models.CharField(max_length=20, null=True,choices=FURNISHED)
    city        = models.CharField(max_length=50, null=True, blank=True)
    street      = models.CharField(max_length=70, null=True, blank=True)
    size        = models.IntegerField(null=True, blank=True)
    beds        = models.CharField(max_length=10, null=True, choices=ROOMS)
    baths       = models.CharField(max_length=10, null=True, choices=ROOMS)
    price       = models.CharField(max_length=10, null=True, blank=True)
    latitude    = models.FloatField(null=True, blank=True)
    longitude   = models.FloatField(null=True, blank=True)
    pic         = models.ImageField(null=True, blank=True)
    ########## those fields are empty because i don't have enoug content to fill them in 
    #thats why all the 3D models and carousel pic are the same#####
    pic2        = models.ImageField(null=True, blank=True)
    pic3        = models.ImageField(null=True, blank=True)
    pic4        = models.ImageField(null=True, blank=True)
    pic5        = models.ImageField(null=True, blank=True)
    glft_file   = models.FileField(null=True, blank=True)
    bin_file    = models.FileField(null=True, blank=True)

    