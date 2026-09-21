# StreamVerse Django Backend

Production-oriented backend for the StreamVerse React/Vite streaming platform.

## Stack
- Django 5.2 + Django REST Framework
- PostgreSQL
- JWT authentication with SimpleJWT
- Celery + Redis for asynchronous email/background jobs
- SMTP mailing for verification and password reset
- Swagger/OpenAPI via drf-spectacular
- Django admin
- CORS support for React frontend
- Media/static support

## Setup
1. Copy `.env.example` to `.env`.
2. Create PostgreSQL database/user or run `docker compose up -d db redis`.
3. Create virtual environment: `python -m venv .venv`
4. Activate it and install: `pip install -r requirements.txt`
5. Run `python manage.py makemigrations`
6. Run `python manage.py migrate`
7. Create seed data: `python manage.py seed_streamverse`
8. Start API: `python manage.py runserver`
9. Start worker in another terminal: `celery -A config worker -l info`

## Docker
`cp .env.example .env`
`docker compose up --build`

API: http://localhost:8000/api/
Swagger: http://localhost:8000/api/docs/
Admin: http://localhost:8000/admin/

## React integration
Set the frontend `.env`:
`VITE_API_URL=http://localhost:8000/api`

The frontend's existing endpoints such as `/auth/login`, `/auth/register`, `/movies`, `/movies/trending`, `/shows`, `/anime`, `/blogs`, `/subscriptions/plans`, `/content/:id/reviews`, `/notifications`, and `/user/profile` are represented by the backend, with JWT-secured user operations.

## Authentication
Register -> email verification -> login -> receive access/refresh JWTs. Send protected requests with:
`Authorization: Bearer <access_token>`

Refresh:
POST `/api/auth/refresh/` with `{ "refresh": "..." }`

Logout:
POST `/api/auth/logout/` with `{ "refresh": "..." }`

## Email
For Gmail SMTP, use an App Password rather than the normal account password. Configure `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, and `DEFAULT_FROM_EMAIL` in `.env`. Celery sends verification and password-reset emails asynchronously.

## Payments
The subscription module creates payment records and provides a clean provider abstraction point. Real Stripe/PayPal/webhook verification should be connected before production billing; the backend intentionally does not pretend a payment succeeded without provider confirmation.

## Production checklist
- Use strong `SECRET_KEY` and production `DEBUG=False`.
- Restrict `ALLOWED_HOSTS` and CORS.
- Put Django behind HTTPS/reverse proxy.
- Store videos in object storage/CDN and return signed URLs where needed.
- Add real payment provider webhooks and signature verification.
- Add rate limiting/WAF, audit logging, monitoring, backups, and CI/CD.
