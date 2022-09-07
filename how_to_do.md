# Activate
1. python3 -m venv venv
2. source venv/bin/activate
3. python3 -m pip install --upgrade pip

# Installation Django
4. pip install django==4.0.7 # Stable 3.2 # Next stable 4.2
5. django-admin startproject config . # Create directory 'config' 
6. python manage.py migrate
7. python manage.py makemigrations
8. python manage.py createsuperuser #user/user ))
9. python manage.py runserver #Starting development server

# Installation Django REST framework
10. pip install djangorestframework
11. pip install markdown       # Markdown support for the browsable AP
12. pip install django-filter  # Filtering support

# Save to requirements.txt
13. pip freeze > requirements.txt

# Created the project named by rest_api
14. django-admin startapp rest_api

# Push to GitHab 
# https://www.django-rest-framework.org/
# Add 'rest_framework' to your INSTALLED_APPS setting.
INSTALLED_APPS = [
    ...
    'rest_framework',
]
# If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. Add the following to your root urls.py file.
urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]


