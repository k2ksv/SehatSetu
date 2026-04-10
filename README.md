# Sehat Setu

Sehat Setu is a Django-based health sector project with separate `frontend` and `backend` folders.

## Main features

- One combined health directory for doctors, hospitals, and medical stores
- Simple appointment request forms for doctors and hospitals
- Nutrition section with healthy diet plans
- Separate login and registration for users and doctors
- MySQL-ready Django configuration with a SQLite fallback for local testing
- Seed command for pseudo healthcare data and demo logins

## Project structure

- `frontend/` stores templates, CSS, JavaScript, and the low-detail cartoon placeholder illustrations
- `backend/` stores Django apps, project settings, migrations, forms, views, and management commands

## Quick start

Run backend commands from inside `backend/`.

```powershell
cd backend
$env:USE_SQLITE="1"
..\.venv\Scripts\python.exe manage.py makemigrations
..\.venv\Scripts\python.exe manage.py migrate
..\.venv\Scripts\python.exe manage.py seed_sehat_setu
..\.venv\Scripts\python.exe manage.py runserver
```

Set the MySQL environment variables in `backend/.env.example` when you want to use MySQL instead of the SQLite fallback.

## Demo accounts

- User login: `user_demo` / `user12345`
- Doctor login: `doctor_demo` / `doctor12345`

## Admin note

Create a Django superuser if you want admin access:

```powershell
cd backend
..\.venv\Scripts\python.exe manage.py createsuperuser
```
