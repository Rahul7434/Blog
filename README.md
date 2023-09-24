# Blog

 This Django project, titled "Blog," is a web application for managing blog posts and user profiles. It includes features for creating, viewing, updating, and deleting blog posts, as well as user registration and profile management.

## Installation & Project Creaction

1. Python Installation
    - Visit the Official Website  https://www.python.org/.
    - Click on the "Download" opion
    - Choose the Python Version
    - select Operationg System
    - Download the Installer
    - Run the Installer
    - Optional: Modify the Path
    - Verify the Installation
2. Django
   - Open a Commant Promot or Terminal
   - Run the commant ```pip install django```  &  For Specific Version ```pip install django==4.2```
   - Verify the Installation  ```python  -m django --version```


3. Run This Command For Creating Project  ```django-admin startproject projectname``` For Example: ```django-admin startproject Blogs``` open Blogs ```cd blogs``` Then create app ```py manage.py startapp app1```

4. Run the  Server ```py manage.py runserver``` it starts a lightweight development web server provided by Django.
    allows us to do this by serving  application on a local development URL (usually http://127.0.0.1:8000/ by default). This makes it easy to test our views, templates, and application logic.

6. ```py manage.py createsuperuser``` For manage admin interface. you can access the admin panel at http://127.0.0.1:8000/admin/ by default.
   
        - blogs
            - blogs
                - __init__.py
                - asgi.py
                - settings.py
                - urls.py
                - wsgi.py
            - app1
                - __init__.py
                - admin.py
                - apps.py
                - forms.py
                - models.py
                - tests.py
                - urls.py (app level url file)
                - views.py
            - media
            - static
                - app1
                   - css
                   - images
                   - js
             - templates
                  -app1
                     - all templates files
             - manage.py

  ### 1 "__init__.py"
      is a special Python file that is used to indicate that the directory it is present in is a Python package. It can contain initialization code for the package, or it can be an empty file. Packages are a way to structure Python's module namespace by using "dotted module names".

  ### 2 "asgi.py" 
  it  will run all your code in a synchronous thread

  ### 3 "setting.py" 
  This file is a crucial configuration file that contains various settings and options for your web application. It defines how your Django project behaves, including database connections, middleware, authentication settings, time zones, and much more.
  ### 4 "urls.py" 
  file is used to define URL patterns and map them to views. When a user makes a request to your application, Django uses the URL patterns defined in urls.py to determine which view function should handle the request.
  
 ### 5 "wsgi.py"
In a Django web application, the WSGI (Web Server Gateway Interface) file, typically named wsgi.py, is used to interface between a web server and your Django application. WSGI is a standard interface that defines how web servers and web applications communicate with each other in the Python ecosystem
