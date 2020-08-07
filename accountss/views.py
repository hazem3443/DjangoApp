from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'accountss/Dashboard.html')

def products(request):
    return render(request, 'accountss/products.html')
    

def customer(request):
    return render(request, 'accountss/customer.html')
