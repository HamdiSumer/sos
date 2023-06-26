from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class District(models.Model):
    DistrictName = models.CharField(max_length=45)
    Coordination = models.CharField(max_length=45)
    Population = models.IntegerField()

    def __str__(self):
        return self.DistrictName


class LogisticsCompany(models.Model):
    CompanyName = models.CharField(max_length=45)
    Phone = models.CharField(max_length=45)

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')


class LogisticsCompanyHasDistrict(models.Model):
    LogisticsCompany_CompanyID = models.ForeignKey(LogisticsCompany, on_delete=models.CASCADE)
    District_DistrictID = models.ForeignKey(District, on_delete=models.CASCADE)
    CostOfOutsource = models.DecimalField(max_digits=15, decimal_places=2)

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')


class Victim(models.Model):
    Name = models.CharField(max_length=225)
    Surname = models.CharField(max_length=225)
    Address = models.CharField(max_length=225)
    PhoneNumber = models.CharField(max_length=45)
    District_DistrictID = models.ForeignKey(District, on_delete=models.CASCADE)


class Request(models.Model):
    RequestTime = models.DateTimeField()
    CurrentStatus = models.CharField(max_length=45)
    DeliveryTime = models.DateTimeField(null=True)
    Victim_RequesterID = models.ForeignKey(Victim, on_delete=models.CASCADE)


class Courier(models.Model):
    Name = models.CharField(max_length=45)
    Surname = models.CharField(max_length=45)
    Phone = models.CharField(max_length=45)
    LicenseType = models.CharField(max_length=45)

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')


class Vehicle(models.Model):
    VehicleType = models.CharField(max_length=45)
    Capacity = models.IntegerField()

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')


class Donator(models.Model):
    Name = models.CharField(max_length=225)
    Surname = models.CharField(max_length=225)
    Phone = models.CharField(max_length=45)

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')


class Donation(models.Model):
    DonationTime = models.DateTimeField()
    DonationDeliveryTime = models.DateTimeField()
    RequestID = models.IntegerField(null=True)
    Donator_DonatorID = models.ForeignKey(Donator, on_delete=models.CASCADE)
    Request_RequestID = models.ForeignKey(Request, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')


class Items(models.Model):
    ItemCategory = models.CharField(max_length=45)
    Amount = models.IntegerField()

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')


class DonationHasItems(models.Model):
    Donation_DonationID = models.ForeignKey(Donation, on_delete=models.CASCADE)
    Items_ItemID = models.ForeignKey(Items, on_delete=models.CASCADE)
    Quantity = models.IntegerField()

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')


class Purchase(models.Model):
    TransactionCost = models.DecimalField(max_digits=15, decimal_places=2)

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')


class Currency(models.Model):
    Name = models.CharField(max_length=225, default='TL')
    ExchangeRate = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'{self.Name}'


class DonationHasCurrency(models.Model):
    Donation_DonationID = models.ForeignKey(Donation, on_delete=models.CASCADE)
    Currency_CurrencyType = models.CharField(max_length=45, null=False)
    Amount = models.IntegerField()

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')


class PurchaseHasItems(models.Model):
    Purchase_PurchaseTransactionID = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    Items_ItemID = models.ForeignKey(Items, on_delete=models.CASCADE)
    Amount = models.IntegerField()
    UnitItemCost = models.DecimalField(max_digits=15, decimal_places=2)

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')


class Supplier(models.Model):
    SupplierName = models.CharField(max_length=45)
    Phone = models.CharField(max_length=45)

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')


class PurchaseHasSupplier(models.Model):
    Purchase_PurchaseTransactionID = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    Supplier_SupplierID = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=False)

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')


class RequestHasItems(models.Model):
    Request_RequestID = models.ForeignKey(Request, on_delete=models.CASCADE)
    Items_ItemID = models.ForeignKey(Items, on_delete=models.CASCADE)
    Quantity = models.IntegerField()

    @property
    def get_item_quantity(self, item_name):
        try:
            request_has_items = self.requesthasitems_set.get(Items_ItemID__Name=item_name)
            return request_has_items.Quantity
        except RequestHasItems.DoesNotExist:
            return ''


class RequestHasLogisticsCompany(models.Model):
    Request_RequesterID = models.ForeignKey(Request, on_delete=models.CASCADE)
    LogisticsCompany_CompanyID = models.ForeignKey(LogisticsCompany, on_delete=models.CASCADE)

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')


class RequestVehiceCourrierAssignment(models.Model):
    Request_RequesterID = models.ForeignKey(Request, on_delete=models.CASCADE)
    Courier_CourierID = models.ForeignKey(Courier, on_delete=models.CASCADE)
    Vehicle_VehicleID = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    DeliveryTime = models.DateTimeField()

    def get_absolute_url(self):
        pass
        # return reverse('blog-home')
