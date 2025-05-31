from django.contrib import admin
from .models import Order
from django.contrib.sites.models import Site

# Register your models here.
admin.site.register(Order)
