import os
from django.shortcuts import render

from catalog.models import Contact


# Create your views here.


def home(request):
    os.system('python3 manage.py last_five')
    contacts = Contact.objects.all()[0]
    return render(request, 'main/home.html', {'contats': contacts})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
    return render(request, 'main/contact.html')
