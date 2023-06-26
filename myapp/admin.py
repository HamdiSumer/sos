from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(District)
admin.site.register(LogisticsCompany)
admin.site.register(LogisticsCompanyHasDistrict)
admin.site.register(Victim)
admin.site.register(Request)
admin.site.register(Courier)
admin.site.register(Vehicle)
admin.site.register(Donator)
admin.site.register(Donation)
admin.site.register(Items)
admin.site.register(DonationHasItems)
admin.site.register(Purchase)
admin.site.register(Currency)
admin.site.register(DonationHasCurrency)
admin.site.register(PurchaseHasItems)
admin.site.register(Supplier)
admin.site.register(PurchaseHasSupplier)
admin.site.register(RequestHasItems)
admin.site.register(RequestHasLogisticsCompany)
admin.site.register(RequestVehiceCourrierAssignment)