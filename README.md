# Course Management API (Django REST Framework)

Converted from a Node.js + MongoDB project to Django REST Framework using default SQLite.

Run locally:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
```

API endpoints:
- POST /api/auth/register
- POST /api/auth/login  (returns access & refresh tokens)
- POST /api/auth/logout (blacklist refresh token)
- POST /api/auth/token/refresh/ (provided by Simple JWT)
- GET/POST /api/courses/
- GET/DELETE /api/courses/<id>/
- POST /api/purchases/  (authenticated user buys a course)
- GET /api/purchases/   (list authenticated user's purchases)
