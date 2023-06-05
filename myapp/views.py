from django.shortcuts import render


def main(request):
    # Your view logic here
    return render(request, 'main.html')


def login(request):
    # Perform login logic
    # ...

    # Redirect to the login page
    return render(request, 'login.html')  # 'login' is the name of the URL pattern for the login page


def register(request):
    # Perform registration logic
    # ...

    # Redirect to the register page
    return render(request, 'register.html')  # 'register' is the name of the URL pattern for the register page


def donation(request):
    # Perform registration logic
    # ...

    # Redirect to the register page
    return render(request, 'donation.html') # 'register' is the name of the URL pattern for the register page


def request_page(request):
    # Perform registration logic
    # ...

    # Redirect to the register page
    return render(request, 'request.html')  # 'register' is the name of the URL pattern for the register page
