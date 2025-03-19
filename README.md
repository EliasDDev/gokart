# Skolprojekt - Go-Kart-bokningswebbplats med Django som backend.

### Ladda ner
`git clone https://github.com/EliasDDev/gokart.git`

### Skapa virtual environment och installera Django:
#### Windows
```
python -m venv venv
.\venv\Scripts\activate.bat
pip install django
```

#### Ubuntu
```
python3 -m venv venv
source venv/bin/activate
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

### Starta servern:
```
python manage.py runserver 0.0.0.0:8000
```
