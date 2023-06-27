import csv

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Victim, District, Donator, Donation, Request, Items, \
    DonationHasItems, RequestHasItems, Currency, DonationHasCurrency, Supplier, Purchase, PurchaseHasSupplier, \
    PurchaseHasItems
import datetime
from datetime import timedelta
import random
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.db import connection


def main(request):
    # Your view logic here
    return render(request, 'main.html')


def administration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Find the user with the given phone number
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        # Authenticate the user with the provided credentials
        if user is not None:
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')

        # Authentication failed, display an error message
        return render(request, 'administrator.html')

    return render(request, 'administrator.html')


def _login(request):
    if request.method == 'POST':
        phone_number = request.POST['phone']
        password = request.POST['password']

        # Find the user with the given phone number
        try:
            user = User.objects.get(username=phone_number)
        except User.DoesNotExist:
            user = None

        # Authenticate the user with the provided credentials
        if user is not None:
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('request')

        # Authentication failed, display an error message
        return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def _logout(request):
    logout(request)
    return redirect('main')


def register(request):
    districts = District.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        district = request.POST.get('district')
        password = request.POST.get('password')

        # Create a new user
        user = User.objects.create_user(username=phone, password=password, first_name=name, last_name=surname)

        district_objects = District.objects.all()
        selected_object = district_objects.filter(id=int(district)).first()

        # Create a new Victim object and assign the user
        victim = Victim(Name=name, Surname=surname, Address=address, PhoneNumber=phone,
                        District_DistrictID=selected_object)

        # Assign the user to the Victim object
        victim.user = user
        victim.save()

        # Automatically log in the user
        login(request, user)

        # Redirect to the request page
        return redirect('request')

    return render(request, 'register.html', {'districts': districts})


def donation(request):
    currencies = Currency.objects.all()

    # Redirect to the register page
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        currency = request.POST.get('currency')

        items_list = ['cash', 'shelter', 'hygiene', 'food', 'clothing', 'medical']

        donated_items = []
        donated_amounts = []

        for i in request.POST:
            if i in items_list:
                donated_items.append(i)
                donated_amounts.append(request.POST.get(i))

        # save donation data
        def _don(donator=None, currency=None):
            start_date = datetime.datetime.now()
            end_date = start_date + timedelta(days=20)
            random_date = start_date + (end_date - start_date) * random.random()

            donation = Donation(DonationTime=datetime.datetime.now(),
                                DonationDeliveryTime=random_date,
                                Donator_DonatorID=donator)

            donation.save()

            # change this to donated item amounts and id's enumerate
            for j in range(len(donated_items)):
                item_list = Items.objects.all()

                item_name = donated_items[j]
                quantity = donated_amounts[j]
                item = item_list.filter(ItemCategory=item_name).first()

                don = DonationHasItems(Donation_DonationID=donation,
                                       Items_ItemID=item,
                                       Quantity=quantity)
                don.save()

                if item_name == 'cash':
                    curr = Currency.objects.get(id=currency)

                    _currency = DonationHasCurrency(Donation_DonationID=donation,
                                                   Currency_CurrencyType=curr.Name,
                                                   Amount=quantity)

                    _currency.save()

            # check if donation is same as request row
            donation_items = DonationHasItems.objects.filter(Donation_DonationID=donation)

            requests = Request.objects.all()

            matching_request_items = False
            match_req_id = None

            for req in requests:
                requested_items = RequestHasItems.objects.filter(Request_RequestID=req)

                if len(donation_items) == len(requested_items):
                    _count = 0
                    for _ in range(len(donation_items)):
                        if (donation_items[_].Items_ItemID.id == requested_items[_].Items_ItemID.id) & (
                                donation_items[_].Quantity == requested_items[_].Quantity):
                            _count += 1
                            continue
                        else:
                            break
                    if _count == len(donation_items):
                        matching_request_items = True
                        match_req_id = req
                        break

            if matching_request_items:
                # If a match is found, assign the request ID to the donation
                donation.RequestID = match_req_id.pk
                donation.Request_RequestID = match_req_id
                donation.save()

            # update database after donation
            for _item in donation_items:
                if _item.Items_ItemID.ItemCategory != 'cash':
                    item_category = Items.objects.get(ItemCategory=_item.Items_ItemID.ItemCategory)
                    item_category.Amount += _item.Quantity
                    item_category.save()
                else:
                    item_category = Items.objects.get(ItemCategory=_item.Items_ItemID.ItemCategory)
                    curr = Currency.objects.filter(id=currency)
                    item_category.Amount = _item.Quantity * curr[0].ExchangeRate

                    item_category.save()

        if phone is not '':

            try:
                donator = Donator.objects.get(Phone=phone)
            except Exception as e:
                donator = None

            if donator is None:
                # save the donator to the database
                _donator = Donator(Name=name, Surname=surname, Phone=phone)
                _donator.save()

                _don(_donator, currency)
        else:
            if (name is None) & (surname is None):
                # dont save the donator, anonym
                _don(currency=currency)
            else:
                # save the donator
                _donator = Donator(Name=name, Surname=surname, Phone=phone)
                _donator.save()

                _don(_donator, currency)

    return render(request, 'donation.html', {'currencies': currencies})


def donation_admin(request):
    donations = Donation.objects.all()
    return render(request, 'donation_admin.html', {'donations': donations})


def inventory_admin(request):
    items = Items.objects.all()
    return render(request, 'inventory.html', {'items': items})


def get_donated_items(request):
    donation_id = request.GET.get('donation_id')
    donation_has_items = DonationHasItems.objects.filter(Donation_DonationID=donation_id)

    donated_item_dict = {}

    for i in donation_has_items:
        item = Items.objects.get(id=i.Items_ItemID_id)
        donated_item_dict[f'{item.ItemCategory}'] = i.Quantity

    # Construct the JSON response
    response_data = {
        'donation_id': donation_id,
        'donated_items': donated_item_dict
    }

    return JsonResponse(response_data)


def procurement_admin(request):
    suppliers = Supplier.objects.all()
    items = Items.objects.all()
    purchases = PurchaseHasSupplier.objects.all()

    # request tamamlama kontrolü de yap!!!!! yukarıda kaldı o

    if request.method == 'POST':
        # inventory cash controlü yetiyor mu? estimated price'ı bunun içine gönder
        cost_estimate = float(request.POST.get('costEstimate'))
        supID = int(request.POST.get('supplier'))
        supplier = Supplier.objects.get(id=supID)
        inv_cash = items.get(ItemCategory='cash')

        itemPrices = {
            'shelter': 594,
            'hygiene': 83,
            'food': 38,
            'clothing': 343,
            'medical': 232
        }

        supplierRates = {
            1: 0.92,
            2: 1.13,
            3: 1.34,
            4: 1.52,
            5: 1.35,
            6: 1.46,
        }

        if cost_estimate <= inv_cash.Amount:
            # we have enough money

            pur = Purchase(TransactionCost=cost_estimate)
            pur.save()

            pur_HS = PurchaseHasSupplier(Purchase_PurchaseTransactionID=pur,
                                         Supplier_SupplierID=supplier)

            pur_HS.save()

            inv_cash.Amount = inv_cash.Amount - cost_estimate
            inv_cash.save()

            items_list = ['cash', 'shelter', 'hygiene', 'food', 'clothing', 'medical']

            ordered_items = []
            ordered_amounts = []

            for i in request.POST:
                if i in items_list:
                    ordered_items.append(i)
                    ordered_amounts.append(request.POST.get(i))

            # update database after order completed
            for _item in range(len(ordered_items)):
                item_category = Items.objects.get(ItemCategory=ordered_items[_item])
                item_category.Amount += int(ordered_amounts[_item])
                item_category.save()

                item_raw_cost = itemPrices[item_category.ItemCategory]
                sup_Rate = supplierRates[supID]

                item_cost = item_raw_cost * sup_Rate

                pur_HI = PurchaseHasItems(Purchase_PurchaseTransactionID=pur,
                                          Items_ItemID=item_category,
                                          Amount=ordered_amounts[_item],
                                          UnitItemCost=item_cost)
                pur_HI.save()

        else:
            # give alert not enough money!
            messages.error(request, "Not enough money in the inventory.")

    return render(request, 'procurement_admin.html', {'suppliers': suppliers, 'items': items, 'purchases': purchases})


def get_purchased_items(request):
    purchase_id = request.GET.get('purchase_id')
    proc_has_items = PurchaseHasItems.objects.filter(Purchase_PurchaseTransactionID=purchase_id)

    bought_item_dict = {}

    for i in proc_has_items:
        item = Items.objects.get(id=i.Items_ItemID_id)
        bought_item_dict[f'{item.ItemCategory}'] = i.Amount

    # Construct the JSON response
    response_data = {
        'proc_id': purchase_id,
        'proc_items': bought_item_dict
    }

    return JsonResponse(response_data)


def reporting_admin(request):
    return render(request, 'reporting_admin.html')


def request_admin(request):
    requests = Request.objects.all()
    return render(request, 'request_admin.html', {'requests': requests})


def get_request_details(request):
    request_id = request.GET.get('request_id')
    request_has_items = RequestHasItems.objects.filter(Request_RequestID=request_id)

    requested_item_dict = {}

    for i in request_has_items:
        item = Items.objects.get(id=i.Items_ItemID_id)
        requested_item_dict[f'{item.ItemCategory}'] = i.Quantity

    # Construct the JSON response
    response_data = {
        'request_id': request_id,
        'request_details': requested_item_dict
    }

    return JsonResponse(response_data)


@csrf_exempt
def delete_request(request):
    if request.method == 'DELETE':
        request_id = request.GET.get('request_id')

        try:
            request = Request.objects.get(pk=request_id)
            request.delete()
            return JsonResponse({'message': 'Request deleted successfully'})
        except Donation.DoesNotExist:
            return JsonResponse({'message': 'Request not found'}, status=404)

    return JsonResponse({'message': 'Invalid request method'}, status=400)


@csrf_exempt
def update_request(request):
    if request.method == 'UPDATE':
        request_id = request.GET.get('request_id')

        request = Request.objects.get(pk=request_id)

        # check whether we can met
        req_items = RequestHasItems.objects.filter(Request_RequestID=request_id)

        for _item in req_items:
            item = Items.objects.get(ItemCategory=_item.Items_ItemID.ItemCategory)

            if _item.Quantity <= item.Amount:
                continue
            else:
                response_data = {
                    'request_id': request_id,
                    'disable_buttons': False
                }
                return JsonResponse(response_data)

        request.CurrentStatus = 'Completed'

        start_date = request.RequestTime + timedelta(days=5)
        end_date = start_date + timedelta(days=30)
        random_date = start_date + (end_date - start_date) * random.random()

        request.DeliveryTime = random_date

        request.save()



        # update database after request completed
        for _item in req_items:
            item_category = Items.objects.get(ItemCategory=_item.Items_ItemID.ItemCategory)
            item_category.Amount -= _item.Quantity
            item_category.save()

        response_data = {
            'request_id': request_id,
            'disable_buttons': True
        }

        return JsonResponse(response_data)


def request_page(request):
    currencies = Currency.objects.all()

    if request.method == 'POST':
        RequestTime = datetime.datetime.now()
        CurrentStatus = 'Incomplete'
        DeliveryTime = None
        Victim_RequesterID = request.user.id

        victim = Victim.objects.get(id=Victim_RequesterID)

        _request = Request(RequestTime=RequestTime, CurrentStatus=CurrentStatus,
                           DeliveryTime=DeliveryTime, Victim_RequesterID=victim)
        _request.save()

        items_list = ['cash', 'shelter', 'hygiene', 'food', 'clothing', 'medical']

        requested_items = []
        requested_amounts = []

        for i in request.POST:
            if i in items_list:
                requested_items.append(i)
                requested_amounts.append(request.POST.get(i))

        for j in range(len(requested_items)):
            item_list = Items.objects.all()

            item_name = requested_items[j]
            quantity = requested_amounts[j]
            item = item_list.filter(ItemCategory=item_name).first()

            request_has_items = RequestHasItems(Request_RequestID=_request,
                                                Items_ItemID=item,
                                                Quantity=quantity)

            request_has_items.save()

    return render(request, 'request.html', {'currencies': currencies})


@csrf_exempt
def delete_donation(request):
    if request.method == 'DELETE':
        donation_id = request.GET.get('donation_id')

        try:
            donation = Donation.objects.get(pk=donation_id)
            donation.delete()
            return JsonResponse({'message': 'Donation deleted successfully'})
        except Donation.DoesNotExist:
            return JsonResponse({'message': 'Donation not found'}, status=404)

    return JsonResponse({'message': 'Invalid request method'}, status=400)