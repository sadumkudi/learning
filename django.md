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
    
3. Features available in Django web framework
    - Admin Interface (CRUD)
    - Templating
    - Form handling
    - Internationalization
    - Session, user management, role-based permissions
    - Object-relational mapping (ORM)
    - Testing Framework
    - Fantastic Documentation
 4. Middlewares in Django 
    - session management
    - user authentication
    - csrf
    - security
    - messaging
 5. Signals in Django
  Signal are inbuilt utility in Django. They allow to execute some piece of code based on some action or event is occurred in framework something like a new user register, on delete of a record. Below is the list of some inbuilt signal in Django
    - pre_save and post_save
    - pre_delete and post_delete
    - pre_request and post_request 
    
  
## Links
1. https://www.youtube.com/watch?v=D6esTdOLXh4
2. https://github.com/hiteshchoudhary/DjangoExercise1
