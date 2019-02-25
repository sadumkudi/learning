### notes
- pip install django
- django-admin startproject projectname - new project
- python manage.py runserver
- python manage.py startapp appname - to create a new app
- file struture:
  - settings.py
    - INSTALLED_APPS
    - MIDDLEWARE
    - TEMPLATES
      - how templates work
      - 'DIRS': [os.path.join(BASE_DIR, 'templates')],
    - DATABASES
    - STATIC_URL
  - urls.py
- in app folder:
  - admin.py
    - configuration file for the built-in admin app
  - apps.py
  - views.py
  - DB migartion
    - python manage.py migrate
    - python manage.py makemigrations appname
    - python manage.py migrate appname
  - Create super user for aadmin
    - python manage.py createsupersuser
  
  
  
  
## Links
1. https://www.youtube.com/watch?v=D6esTdOLXh4
