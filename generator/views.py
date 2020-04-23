from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnoprwsyzx')
    length = 10

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPRWSYZX'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_+-'))

    length = int(request.GET.get('length', 12))

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
