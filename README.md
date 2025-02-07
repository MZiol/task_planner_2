Wymagania
Przed uruchomieniem aplikacji upewnij się, że masz zainstalowane poniższe zależności:

Python 3.8+
Django 4.x+
PostgreSQL
pip (do instalacji pakietów Pythona)
Instalacja

1. Skopiuj repozytorium

git clone https://github.com/yourusername/task-management-app.git

2. Stwórz i aktywuj wirtualne środowisko
Utwórz wirtualne środowisko, aby izolować zależności projektu:

python3 -m venv venv
venv\Scripts\activate     # Na systemie Windows

3. Zainstaluj wymagane biblioteki
Zainstaluj wszystkie wymagane biblioteki Pythona za pomocą pip:

pip install -r requirements.txt
Plik requirements.txt powinien zawierać wszystkie potrzebne pakiety

4. Skonfiguruj bazę danych PostgreSQL
Upewnij się, że masz zainstalowaną bazę danych PostgreSQL. Stwórz nową bazę danych i użytkownika dla aplikacji. W terminalu PostgreSQL wykonaj następujące kroki:

psql -U postgres
Utwórz bazę danych:

CREATE DATABASE task_manager;
Utwórz użytkownika bazy danych:

CREATE USER task_user WITH PASSWORD 'password';
Przyznaj odpowiednie uprawnienia:

GRANT ALL PRIVILEGES ON DATABASE task_manager TO task_user;
Wyjdź z PostgreSQL:

\q
5. Skonfiguruj połączenie z bazą danych
W pliku settings.py aplikacji Django zmodyfikuj sekcję DATABASES, aby wskazać swoją bazę danych PostgreSQL:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'task_manager',
        'USER': 'task_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

6. Przeprowadź migracje bazy danych
Przed uruchomieniem aplikacji musisz przeprowadzić migracje bazy danych:

python manage.py makemigrations
python manage.py migrate

7. Stwórz superużytkownika (opcjonalnie)
Aby uzyskać dostęp do panelu administracyjnego Django, stwórz superużytkownika:

python manage.py createsuperuser
Postępuj zgodnie z instrukcjami, aby wprowadzić nazwę użytkownika, email i hasło.

8. Uruchom serwer Django
Na tym etapie aplikacja jest gotowa do uruchomienia. Możesz uruchomić lokalny serwer deweloperski Django:

python manage.py runserver
Serwer będzie działał na http://127.0.0.1:8000/. Możesz teraz uzyskać dostęp do swojej aplikacji.

9. Testowanie API
Aby przetestować API, użyj narzędzia do wysyłania zapytań HTTP, takiego jak Postman lub Insomnia.

Przykładowe endpointy API:

GET /api/tasks/ – Pobierz wszystkie zadania
POST /api/tasks/ – Tworzenie nowego zadania
GET /api/tasks/{id}/ – Szczegóły konkretnego zadania
PUT /api/tasks/{id}/ – Edycja zadania
DELETE /api/tasks/{id}/ – Usuwanie zadania
GET /api/tasks-history/ – Historia zmian zadania
Środowisko produkcyjne
W przypadku wdrożenia aplikacji w środowisku produkcyjnym, upewnij się, że:

Używasz odpowiedniego serwera (np. Nginx, Gunicorn).
Włączasz SSL, aby zabezpieczyć połączenie.
Zmieniasz ustawienia bazy danych na produkcyjne (np. konfiguracja bazy danych na serwerze).
Ustawiasz DEBUG = False w settings.py.
Zarządzasz plikami statycznymi i mediami (np. za pomocą collectstatic).
