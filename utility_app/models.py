from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128)


TYPES = [
    ('fundacja', 'fundacja'),
    ('organizacja pozarządowa', 'organizacja pozarządowa'),
    ('zbiórka lokalna', 'zbiórka lokalna'),
]


class Institution(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.CharField(max_length=32, choices=TYPES)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=16)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
