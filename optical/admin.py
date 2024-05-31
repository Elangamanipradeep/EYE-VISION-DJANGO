from django.contrib import admin
from .models import *


# For Contact form 
admin.site.register(Contact)


# For Order Form 
admin.site.register(Orders)

# #For products
# admin.site.register(Products)