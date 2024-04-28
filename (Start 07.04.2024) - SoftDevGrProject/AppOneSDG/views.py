from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

testdata = [
    {'id':1, 'name': 'Item 1 of list'},
    {'id':2, 'name': 'Item 2 of list'},
    {'id':3, 'name': 'Item 3 of list'},
    {'id':4, 'name': 'Item 4 of list'},
    {'id':5, 'name': 'Item 5 of list'},
    {'id':6, 'name': 'Item 6 of list'},
]

def home(request):
    return render(request, 'AppOneSDG/home.html', {'testdata':testdata})

def blist(request):
    return render(request, 'AppOneSDG/blist.html')

def navbar(request):
    return render(request, 'navbar.html')