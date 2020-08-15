# DjangoApp

## ***about Django***

Django is a Python-based free and open-source web framework that follows the model-template-view (MVC) architectural pattern

## ***Setup***
~~~
$ pip3 install Django=3.1
~~~

## ***Starting a Project***
to start a project run command
~~~
$ python3 manage.py startproject
~~~
in this directory you will find files such as :

- manage.py -> this file contain the calls the commands that is been used to generate framework files and help building our website all commands passed here is being passed to Django engine to generate all required files for the task we want to do

- urls.py -> contain redirected routes all routes should be included here or reference new route list from app urls file to this main urls file

- settings.py -> contain all settings for our website such as db configurations and static folder path and media url path for including video or images

to run the compiled code run this command
~~~
$ python3 manage.py runserver
~~~
## ***starting an App***
~~~
    $python3 manage.py startapp appname
~~~
this command will generate a directory with the app name having all nessessary file to build MVC files for you so you can concentrate on app functionality ,these files are:
- ***asgi.py, wsgi.py*** -> the application server uses to communicate with your code. It’s commonly provided as an object named application in a Python module accessible to the server.
The startproject command creates a file <project_name>/asgi.py that contains such an application callable.
It’s not used by the development server (runserver), but can be used by any ASGI server either in development or in production.

- ***app.py*** -> defines app name within you project

- ***views.py*** -> contain all function based or object based templates that is redirected by urlpatterns list to return certain html templates 

- ***tests.py*** -> handle all test cases for a certain task in the app

- ***models.py*** ->all obejct mapped tables and db relations goes into that file to be mapped to db queries

also generates other files we talked about earlier ***settings.py, urls.py***

also you can generate folders for templates of each app within your app folder and static files can also served from your root directory with ```{% load static %}``` at the top of your template also note you should include it each time on each folder you want to call static files into and provide a directory of static folder in settings.py file with static url 
and provide 
## ***urls***
to redirect to the certain template first you need to write it down in the urlpatterns list
~~~
    path('',include('accountss.urls')),
~~~
then in the  accountss folder in the urls.py file you can include your urls as previous and in views define functions or classes and call these in the urls file 
such that
```
urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
]
```

## ***Views***

then to render certain template file in views first we have to create templates in our app dir with pages template and here we can inherite templates into others to provide more maintainability and extensibility such that 

in the ***main.html*** file we need to include ***navbar.html*** such that
```
{% include 'accountss/navbar.html'%}
```
this will include this file as many as i want by repeating this line 
but to extend or inherite a template in many templates or html files you first have to provide a block content in the ***main.html*** file such that
```
{% block content %}
        
{% endblock %}
```
and to extend the ***main.html*** into other files you can do it such that

```
{% extends 'accountss/main.html'%}

{% block content%}
<!-->html tags that is going to be writen goes here<-->
{% endblock %}

```

and within the html code you can call 
```
{% include %}
```
to include other templates as many as you want

also to serve static files you should provide a link in the header of main project with 
```
{% load static %}
```
to force Django engine to look for static directory and map it's css and js files into our tempaltes also you should provide a link such that
```
        <link rel="stylesheet" type="text/css" href="{% static '/css/main.css' %}">

```
and each time you have a new css file or js file you shold add a link to it in the head of ***main.html*** file

 ***notice here***
 that each time you call an image or video to go to it's dir
first you should provide 
```
MEDIA_URL = '/images/'
```
in the ***settings.py*** file

then you should load static as we talked earlier 
```
{% load static %}
```
 then provide a path to your image such that
```
  <img class="nav-small-hazem" src="{% static 'images/logo.png' %}">
```

## ***models***

models are object database schema that is going to be reflected in database as tables and Django creates any of them for us for authentication login and we first need to ***migrate*** these changes which mean ***commanding database engine to updateing database tables with latest schema for our tables that we changed***
and log back the tables migrated

to run migrations
```
$ python3 manage.py migrate
```
this command migrates default database structure and because we are running on sqlite we don't have way to see these tables so we need to create a super user to use Django admin panel to view these data

now let's look at ***models.py*** within app directory

we can add object based tables schema such that
```
class Customer(models.Model):
    name  = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
```
this class inherite from models the database types and keywords that helps you identify the table columns.

this will create a table with name **appname_tablename** which will be accountss_customer, this table will have columns **id, name, phone, email, date_created** the first id column is an auto generated column to indicate records insertion within the table with a unique id which is an incremental number starting from 1 then the column date_created is auto inserted in the database while insertion 

- then after saving this file you need to run migrations with these two commands
    - `$ python3 manage.py makemigrations`
    this command creates new schema to changes that is going to be uploaded to database 
    
    - `$ python3 manage.py migrate`
    this update upload the changes to database and actually create or modify the tables there(in the daatbase file)

then to be able to see these changes with admin panel you need to register this table to the *admin.py* file such that
```
from .models import Customer 

admin.site.register(Customer)
```
then on the **/admin** url you can CRUD new records in the table 
also you can use this below code on class 
```
def __str__(self):
        return self.name
``` 
to return the name of a certain field this is used by admin panel to show the name of each column in panel table view


also you can constrain the fields with certain value by creating a list such that
```
STATUS = (
        ('Pending','Pending'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
```
***noteice here*** that the right value is the displayed value and the left one is the actually stored one

and assign this values to certain column such that
```
    status = models.CharField(max_length=200, null=True, choices=STATUS)
```

- one to many Relationship is handeled as we know by a foreignkey constrain and admin panel understands these relationships
we can do foreignKey such that
    ```
    within order class
        product  = models.ForeignKey(Product,   null=True, on_delete=models.SET_NULL)
    ```

    this need to be linked with ***on_delete*** method to set this record in Product table with null when the reference value(Primary Key) in product class is being removed also see those:

    - CASCADE: When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.

    - PROTECT: Forbid the deletion of the referenced object. To delete it you will have to delete all objects that reference it manually. SQL equivalent: RESTRICT.

    - RESTRICT: (introduced in Django 3.1) Similar behavior as PROTECT that matches SQL's RESTRICT more accurately. (See django documentation example)

    - SET_NULL: Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user. SQL equivalent: SET NULL.

    - SET_DEFAULT: Set the default value. SQL equivalent: SET DEFAULT.

    - SET(...): Set a given value. This one is not part of the SQL standard and is entirely handled by Django.

    - DO_NOTHING: Probably a very bad idea since this would create integrity issues in your database (referencing an object that actually doesn't exist). SQL equivalent: NO ACTION.

- Many To Many relationship in handled within by a table that matches tags for each product by third table that maps them the Django handles this automatically with this creation of Tags class such that
```
class Tag(models.Model):
    name  = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
```
that only takes the tag name
and the Django engine generates product_tags table that saves each product with each tags
in the product table you need add a link to that relationship within the Product class such that 
```
within Product class
    tags = models.ManyToManyField(Tag)
```

### ***Quering data***
- in Chile-parent model you can find data up/down using object mapping methods such that
Suppose we have two classes parent class and chile one such that

```
class parent(models.Model):
    name = models.charfield(....)

class child(models.Model):
    parent = modelsForeignKey(parent)
    ....

```
then you can go down by finding childs of the parent such that
```
parent1 = parent.objects.first()
childs_of_parent1 = parent1.child_set.all()
```
also you can go up by finding info about the child such that
```
child1 = child.objects.get(id=2)
print(child1.id,child1.phone) 
or
print(child1.parent.name) #this will print the name from parent table that have child id = 2
```

- to filter the data you can do it such that
```
parent.objects.filter(name="hazem")
```
if you leave the filter empty it will act as .all() and return all elements in the table

you can also chaining them such that:
```
parent.objects.filter(name="hazem",id=1)
```

-to order elements according to columns do such that
```
parents = parent.objects.all().order_by('id')
```
and to order in reverse order do that
```
parents = parent.objects.all().order_by('-id')
```

- to order data of many-many relationship such as listing products with tag "sports"
you can start from .ManyToManyField() instance link and go up such that
```
products = Product.objects.filter(tags__name="Sports")
``` 
this will search for the tags named "Sports" and matches that with Products and filters it with tag named "Sports"

if the record is countable we can count that by .count method or looping through out them and counting to a dictionary of all elements existed per that record field

<hr>

## Template Tags 

related to views

it a way for us to write python code like logic in our templates to output data
- for loops in a template 
```
{% for i in range(5) %}
    <tr>
        <td></td>
    </tr>
{% endfor %}
``` 
-variables comming from rendered views
```
<td> {{ customer.name }} </td>
```

also you need to pass these variables within the ***views.py*** file and pass the data to the rendered template also don't forget to include models file to be able to interact with db models such that 

```
...
from .models import *
...

within products model
... 
    products = Product.objects.all()
    
    return render(request, 'accountss/products.html', {'products':products})
    ...

```
and within the template you need to do such that

```
{% for i in products %}
    <tr>
        <td>
            {{ i.name }}
        </td>
        <td>
            {{ i.category }}
        </td>
        <td>
            {{ i.price }}
        </td>
    </tr>
{% endfor %}
```
also you can pass the context variable containing all values such that

```
orders = Order.objects.all() 
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()

    delivered = orders.filter(status= 'Delivered').count()
    pending = orders.filter(status= 'Pending').count()

    context = {'customers':customers, 'orders':orders, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
    return render(request, 'accountss/Dashboard.html',context)
```

and within the template you can call these dictionary elements by their direct name because context is parsed with Django as main template context such that
```
{% for customer in customers %}
    <tr>
        <td></td>
        <td>{{ customer.name }}</td>
        <td>{{ customer.phone }}</td>
    </tr>
{% endfor %}
and so on ...
```
## Dyanamic Url Routing & dynamic templates
we can pass data into the url and render data according to these data within **urls.py** such that
```
    path('customer/<str:pk>', views.customer),
```
here we declared a string variable called pk we also can define variables such that
```
<int:variable_name>
<slug:variable_name> 
``` 
slug is a small string sentence

then within the **views.py** file you need to receive this variable such that
```

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    ...
```
and do what ever you want with it and render it back to the tempalte

*** Notice *** 
when dealing with models it links foreign key values with it's primary key table so you can select elements by their linked tables

now to make your url more dynamic you can add an argumant **name** to path method in **urls.py** file such that
```
    path('products/', views.products,name='products'),
```
this will enable you to call the template by it's name even if you change the url itself
so to call this dynamic url in templates you can do such that
```
{% url 'name' val.id %}
{% url 'customer' customer.id %}
```
so if you change the url to 'customer_data' it will be updated automatically 

and this makes your links in the templates also dynamic with any change in the links layout

## **CRUD functionality to a certain model**

### **Create**
it is a list of steps that is related to writing to database in a proper way there are different way to do that and this way called Model Form 

- first we need to create the Form class that is going to inherite from ModelForm class that have all methods that are going to help us insert into our db such as **.save** method which saves data to db **is_valid** this is going to check our csrf token also the form itself contains the fields we are going to submit with choices we choose, and takes in the db model , but don't forget to import the model such that 
```
...
from .models import Order
...

class OrderForm(ModelForm):    
    class Meta:
        model = Order
        
        fields = '__all__' #['customer','product']
        
        label = {
            'customer': _('الزبون'),
            'product': _('المنتج'),
            'status': _('حالة المنتج'),
        }
        
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        print("hellos")
        self.fields["customer"].choices = [("", "please choose value"),] + list(self.fields["customer"].choices)[1:]        
        self.fields["product"].choices = [("", "please choose value"),] + list(self.fields["product"].choices)[1:]        
        self.fields["status"].choices = [("", "please choose value"),] + list(self.fields["status"].choices)[1:]
```
after importing models we can create a class of our submitted form calling it **OrderForm** this class contains class meta which have model and fields choosen from that model that is going to be inserted and submitted back to the user then you can edit labels of these fields to be something else than column name also for foreign keys it creates multichoice field (combobox) that is going to be selected and submitted, by default it creates that field for foreign key values and you can change default message by extending the class constructor with all of it's code there in the ModelForm class

- second you need to create the view & route for that page that is going to use that class we just created but for our view here we need to under stand something that when we create a form into our page this form is loaded with user inserted data then is going to sent back with **POST** request so here we first need to create a form with csrf token to check validation of the form we sent to the user to avoid cross site request forgery attack then when the user fill in the form and sent it back to the server posted data is saved in request object and server checkes that form and writes it to db and creates new form with the written data to it, then redirect to home page

so in our **views.py**

```
....
from .forms import OrderForm

def createOrder(request):
    form = OrderForm() #this is for the first form creation according to fields in the form
    if request.method == 'POST':
        print('form is: ',form)
        # print('this is post: ',request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            print("Errors are: ",form.errors)
            form.save() 
            return redirect('/')

    context = {'form':form}
    return render(request, 'accountss/order_form.html',context)
```
notice here that the view returns **order_form** which we will talk about in thirdstep
also the route for that view is
```
    path('create_order/', views.createOrder, name='create_order'),
``` 
- third we need to create the template of the form that is going to be submitted first the ModelForm we inherited from makes the form for us but here we need to submit it to the server and generate the tamplate we want we can easily call **{{form}}** and it will be added directly to the template or we can call form members individually and style it as we want such that:
    - {{form.customer.name}} ->this gets the column model name 
    
    - {{ form.customer.label }} ->this gets the label name that you specified in the form class

    - {{ form.customer.help_text }} ->this gets help text of field you specified help text to

    - {{ form.customer }} -> this gets the input field to be submitted 
    
    - also there is a help message that can be added within 
    
also you can loop over form fields but you should take care of fields name while submitting the form and you can edit default html tags with this method of form creation and you can add **required** alert messages, this is **order_form.html**template which extends from main template:
```
{% extends 'accountss/main.html'%}

{% load static %}

{% block content %}

<form action="" method="POST">

    {% csrf_token %}
    
    <label> {{ form.customer.label }} </label>
    <select name="{{form.customer.name}}" required oninvalid="this.setCustomValidity(this.value ? '' : 'برجاء ادخال اسم الزبون');" >
        {% for select in form.customer %}
            {{ select }}
        {% endfor %}
    </select>
    <br>
    
    <label> {{ form.product.label }} </label>
    <select name="{{form.product.name}}" required oninvalid="this.setCustomValidity(this.value ? '' : 'برجاء ادخال المنتج');" >
        {% for select in form.product %}
            {{ select }}
        {% endfor %}
    </select>
    <br>

    <label> {{ form.status.label }} </label>
    <select name="{{form.status.name}}" required oninvalid="this.setCustomValidity(this.value ? '' : 'برجاء ادخال حالة المنتج');">
        {% for select in form.status %}
            {{ select }}
        {% endfor %}
    </select>
    <br>
    <!-- {{ form.customer.error_messages }} -->

    <input type="submit" name="Submit" value="حفظ" onclick="this.click();" >
</form>
{% endblock %}
```

### **Update**
as we did with create and this update will use the same template 
- first let's create a view and url for that update functionality 
but here the update will need a foreignkey value to get data of this id from db and fill in this data into our form and pass these to our template 
so to create this view in **view.py** :
```
def updateOrder(request, pks):
    order = Order.objects.get(id=pks)
    form = OrderForm(instance=order)
    print("sss: ",order)
    context = {'form':form}
    if request.method == 'POST':
        print('this is post: ',request.POST,"instance: ",order)
        form = OrderForm(request.POST, instance=order)#here you need to pass the same instance to inforce save method to update old instance of order model not to create a new one
        if form.is_valid():
            print("Errors are: ",form.errors)
            form.save()
            return redirect('/')

    return render(request, 'accountss/order_form.html',context)
```
but notice here we first get data by id that we will get from update button on the dashboard then pass this instance of data into a new **OrderForm** and then passes this data to our template whcih is the same template of create but this time form is preloaded with data in db then to proceed the update we did as we did with create functionality but this time we need to pass the same instance we already got to force the **.save** method to update not to create 

just that for now and no need here to create a form class or any templates actually if you want you can do that and change the template but as soon as you update the inserted values so why creating a new template ? :D also you can **false commit changes** before actually updating to db and change the commited instance and commit these new changes to db only if you do some logic before updating or override user data according to some inputs

### **Delete**
to perform delete operation you need to log a message to the user to ensure that he want to delete this item and this form should be csrf protected so 

- first we need to create **delete.html** form which is going to be ask user to confirm delete operation such that
```
{% extends 'accountss/main.html'%}
{% load static %}
{% block content %}

<p>Are you sure you want to delete {{item}}?</p>

<form method="POST">
    {% csrf_token %}
    <a href="{% url 'home' %}">Cancel</a>
    <input type="submit" name="Confirm">
</form>
{% endblock %}
```
this form extends main form and submit a post request to the concerned view (deleteOrder)

- second we need to create the view and the url that is going to be directed to and this url will be called by order id form dashboard
first the view is such that :
```
@requires_csrf_token
def deleteOrder(request,pkd): 
    item = Order.objects.get(id=pkd)
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'accountss/delete.html', context)
```
the **@requires_csrf_token** is for csrf validation on that view then to perform delete operation we need to get instance by id then if the POST request is sent back to this template with valid csrf token the the user has confirmed the delete operation so delete it with **delete()** method 

## inline-form sets
this saves and updates and deletes many forms in one form operation or formset 
- first we need to create a template such that :
```
{% extends 'accountss/main.html'%}

{% load static %}

{% block content %}
<div class="row">
    <div class="col-md-6">
        <div class="card card-body">

            <form action="" method="POST">

                {% csrf_token %}
                {{ formset.management_form }}
                {% for form in formset %}
                    {{form}}
                    <br>
                {%endfor%}
                <input type="submit" name="Submit" value="حفظ" onclick="this.click();" >
            </form>
        </div>
    </div>
</div>

{% endblock %}

```
- then we need to create views and urls such that in **view.py** with it's import
```
....
from django.forms import inlineformset_factory
....

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

``` 
in this file we notice **inlineformset_factory** which creates the class architecture that we will create an instance or object of that class then interact with it as you did with form class and you can loop over it in the template and to style data freely you can add  **{{ formset.management_form }}** It is used to keep track of how many form instances are being displayed and to keep track of which one is being edited and post it's data


