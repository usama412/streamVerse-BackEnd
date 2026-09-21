# API examples

## Register
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H 'Content-Type: application/json' \
  -d '{"username":"usama","email":"you@example.com","password":"StrongPass123!","first_name":"Usama","last_name":"Ahmad"}'
```

## Login
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H 'Content-Type: application/json' \
  -d '{"email":"you@example.com","password":"StrongPass123!"}'
```

## Protected request
```bash
curl http://localhost:8000/api/auth/me/ \
  -H 'Authorization: Bearer ACCESS_TOKEN'
```

## Search
```bash
curl 'http://localhost:8000/api/movies/search/?q=action'
```
