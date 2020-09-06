from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django import forms


from .models import *

from .forms import OrderForm, CreateUserForm

from .filters import orderfilter

from django.core.paginator import Paginator

# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        nextt = request.GET.get('next', '/default/url/')

        if request.method == 'POST':
            if request.POST.getlist('agree-term'):
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    #login new created user
                    username = request.POST.get('username')
                    password = request.POST.get('password1')
                    user = authenticate(request, username=username, password=password)
                    login(request, user)
                    if nextt:
                        return redirect(nextt)
                    else:
                        return redirect('home')
                    # messages.success(request, 'Account Created')
                    # return redirect('loginPage')
            else:
                messages.success(request, 'Please agree all statments to be able to log in')
        context = {'form':form}
        return render(request, 'accountss/RegisterANDlogin_Templates/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        nextt = request.GET.get('next', '/default/url/')
        
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.POST.getlist('remember-me'):
                    request.session.set_expiry(1209600*10)
                    print("cheched:time:8")
                else:
                    request.session.set_expiry(0)
                    print("not checked")

                if nextt:
                    return redirect(nextt)
                else:
                    return redirect('home')
 
            else:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Wrong Password")
                else:
                    messages.info(request, "this user is not signed up")
        return render(request, 'accountss/RegisterANDlogin_Templates/login.html')

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

@login_required(login_url='loginPage')
def home(request):
    orders = Order.objects.all() 
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()

    delivered = orders.filter(status= 'Delivered').count()
    pending = orders.filter(status= 'Pending').count()

    context = {'customers':customers, 'orders':orders, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
    return render(request, 'accountss/Dashboard.html',context)

@login_required(login_url='loginPage')
def products(request):
    products = Product.objects.all()
    
    paginator = Paginator(products, 1)
    current_page_number = request.GET.get('page')
    page_obj = paginator.get_page(current_page_number)
    
    print(paginator.num_pages)
    print(current_page_number)
    if current_page_number :
        if int(current_page_number) > (paginator.num_pages) or int(current_page_number) <= 0:
            print("page not found")

    return render(request, 'accountss/products.html', {'page_obj': page_obj, 'page_number':current_page_number})

@login_required(login_url='loginPage')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    orders_count = orders.count()

    myfilter = orderfilter(request.GET, queryset=orders)
    orders = myfilter.qs

    context = {'customer':customer, 'orders':orders,'orders_count':orders_count,'myfilter':myfilter}
    return render(request, 'accountss/customer.html', context)

@requires_csrf_token
@login_required(login_url='loginPage')
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
@login_required(login_url='loginPage')
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
@login_required(login_url='loginPage')
def deleteOrder(request,pkd): 
    item = Order.objects.get(id=pkd)
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'accountss/delete.html', context)

@requires_csrf_token
@login_required(login_url='loginPage')
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
