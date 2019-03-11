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
  
## Questions
1. Django follows MVC -MVT architecture. MVT  stand for Model View Template design Pattern which is little bit different from MVC (Model View Controller ) Pattern.
2. Components of Django
    - Models.py file: This file defines your data model by extending your single code line into full database tables and add a pre-built administration section to manage content.
    - Urls.py file: It uses a habitual expression to confine URL patterns for processing.
    - Views.py file: It is the main part of Django. The actual processing happens in view
  
  
## Links
1. https://www.youtube.com/watch?v=D6esTdOLXh4
2. https://github.com/hiteshchoudhary/DjangoExercise1
