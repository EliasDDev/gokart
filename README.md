# Skolprojekt: Go-Kart-bokningswebbplats med Django som backend

### Ladda ner projektet:
```
git clone https://github.com/EliasDDev/gokart.git
```

### Skapa virtual environment och installera Django:
#### Windows:
```
python -m venv venv
.\venv\Scripts\activate.bat
pip install django
```

#### Linux:
```
python3 -m venv venv
source venv/bin/activate
pip install django
```

### Uppdatera databasen:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Skapa admin användare:
```
python3 manage.py createsuperuser
```

### Starta servern:
```
python3 manage.py runserver
```
```
nohup python3 manage.py runserver 0.0.0.0:8000 &
```
