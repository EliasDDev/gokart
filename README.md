KÖR KOMMANDOT .\venv\Scripts\activate.bat VID PROJEKT UPPSTART

python -m venv venv
.\venv\Scripts\activate.bat
pip install django
django-admin startproject gokart
cd gokart
python manage.py startapp app

gokart/settings.py:
Lade till "app" i INSTALLED_APPS.

gokart/urls.py:
Lade till "app.urls" i urlpatterns.

app/models.py:
Här beskriver vi våran databas.
python manage.py makemigrations
python manage.py migrate

app/admin.py:
Registrera databas modeller för admin panelen.

Skapa admin användare:
python manage.py createsuperuser
Username: elias
Password: password

Starta servern:
python manage.py runserver