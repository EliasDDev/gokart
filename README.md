# Skolprojekt - Go-Kart-bokningswebbplats med Django som backend.

### Ladda ner
`git clone https://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@github.com/eliasddev/gokart.git`

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
