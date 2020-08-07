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