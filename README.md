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

### ***notice here***
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
