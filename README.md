# Skolprojekt – Go-Kart-bokningswebbplats med Django som backend.

### Skapa virtual environment och installera Django:
```
python -m venv venv
.\venv\Scripts\activate.bat
pip install django
```

### Uppdatera databasen:
```
python manage.py makemigrations
python manage.py migrate
```

### Skapa admin användare:
```
python manage.py createsuperuser
```

### Starta servern (localhost):
```
python manage.py runserver
```

### Starta servern
```
python manage.py runserver 0.0.0.0:8000
```
