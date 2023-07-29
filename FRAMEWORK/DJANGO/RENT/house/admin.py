from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Landlord)
admin.site.register(Tenant)
admin.site.register(Cite)
admin.site.register(Apartment)
admin.site.register(Studio)
admin.site.register(Room)