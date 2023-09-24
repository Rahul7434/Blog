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


## Project Structure
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


# Usage

1. Run This Command For Creating Project  ```django-admin startproject projectname``` For Example: ```django-admin startproject Blogs``` open Blogs ```cd blogs``` Then create app ```py manage.py startapp app1```

  
2. ```py manage.py makemigrations``` (it will generate python code to the sql query) Then ```py manage.py migrate```(it will save the all sql generated code in database).
  
3. Run the  Server ```py manage.py runserver``` it starts a lightweight development web server provided by Django.
allows us to do this by serving  application on a local development URL (usually http://127.0.0.1:8000/ by default). This makes it easy to test our views, templates, and application logic.

4. ```py manage.py createsuperuser``` For manage admin interface. you can access the admin panel at http://127.0.0.1:8000/admin/ by default.

 ##  When you Run the server it will give http://127.0.0.1:800/ Url copy this URL and run on any  browser, but your server must be running.
 ![Like This](https://drive.google.com/file/d/1fTuIS0rU3gVy2D2S1jSU2U4zemKetCUD/view?usp=drivesdk )
