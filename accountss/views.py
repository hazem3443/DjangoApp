from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from .models import *

from .forms import OrderForm

# Create your views here.
def home(request):
    orders = Order.objects.all() 
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()

    delivered = orders.filter(status= 'Delivered').count()
    pending = orders.filter(status= 'Pending').count()

    context = {'customers':customers, 'orders':orders, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
    return render(request, 'accountss/Dashboard.html',context)

def products(request):
    products = Product.objects.all()
    
    return render(request, 'accountss/products.html', {'products':products})
    
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {'customer':customer, 'orders':orders,'orders_count':orders_count}
    return render(request, 'accountss/customer.html', context)

@requires_csrf_token
def createOrder(request):
    form = OrderForm() #this is for the first form creation according to fields in the form
    if request.method == 'POST':
        # print('this is post: ',request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            print("Errors are: ",form.errors)
            form.save() 
            return redirect('/')

    context = {'form':form}
    return render(request, 'accountss/order_form.html',context)

@requires_csrf_token
def updateOrder(request, pku):
    order = Order.objects.get(id=pku)
    form = OrderForm(instance=order)
    context = {'form':form}
    if request.method == 'POST':
        print('this is post: ',request.POST,"instance: ",order)
        form = OrderForm(request.POST, instance=order)#here you need to pass the same instance to inforce save method to update old instance of order model not to create a new one
        if form.is_valid():
            print("Errors are: ",form.errors)
            form.save()
            return redirect('/')
    return render(request, 'accountss/order_form.html',context)

@requires_csrf_token
def deleteOrder(request,pkd): 
    item = Order.objects.get(id=pkd)
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'accountss/delete.html', context)

@requires_csrf_token
def createMultipleOrder(request,pkm):
    customer = Customer.objects.get(id=pkm)
    ordersCount = Order.objects.filter(customer=pkm).count()
    orderFormSet = inlineformset_factory(Customer, Order, fields =('product', 'status'),extra=1 )
    formset = orderFormSet(instance = customer) #also you can add queryset=Order.objects.none() , to delete prefilled values 
    print("ss",ordersCount)
    if request.method == 'POST':
        formset = orderFormSet(request.POST,instance = customer)
        if formset.is_valid():
            formset.save() 
            return redirect('/customer/'+pkm)

    context = {'formset':formset}
    return render(request, 'accountss/Create_multiple_orders_form.html',context)
