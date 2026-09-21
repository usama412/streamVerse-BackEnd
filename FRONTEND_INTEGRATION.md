# React Frontend Integration

Set in the StreamVerse React project:

```env
VITE_API_URL=http://localhost:8000/api
```

## Axios JWT interceptor

Use an axios instance that stores `access` and `refresh` tokens after login. Add:

```ts
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("streamverse_access");
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});
```

Login request:

```ts
const { data } = await api.post("/auth/login/", {
  email,
  password,
});
localStorage.setItem("streamverse_access", data.access);
localStorage.setItem("streamverse_refresh", data.refresh);
```

Register:

```ts
await api.post("/auth/register/", {
  username,
  email,
  password,
  first_name,
  last_name,
});
```

Profile:

```ts
await api.get("/auth/me/");
```

Refresh:

```ts
await api.post("/auth/refresh/", {
  refresh: localStorage.getItem("streamverse_refresh"),
});
```

## Endpoint mapping

| Frontend feature | API |
|---|---|
| Login | POST `/auth/login/` |
| Register | POST `/auth/register/` |
| Current user | GET `/auth/me/` |
| Verify email | POST `/auth/verify-email/` |
| Forgot password | POST `/auth/forgot-password/` |
| Reset password | POST `/auth/reset-password/` |
| Movies/content | GET `/movies/` |
| Trending | GET `/movies/trending/` |
| Search | GET `/movies/search/?q=...` |
| Genres | GET `/genres/` |
| People | GET `/people/` |
| Live | GET `/live/` |
| My List | GET/POST/DELETE `/user/my-list/` |
| History | GET/POST/PATCH/DELETE `/user/history/` |
| Clear history | DELETE `/user/history/clear/` |
| Reviews | GET/POST `/content/{id}/reviews/` |
| Plans | GET `/subscriptions/plans/` |
| Checkout record | POST `/subscriptions/checkout/` |
| My subscriptions | GET `/subscriptions/` |
| Blogs | GET `/blogs/` |
| Notifications | GET `/notifications/` |
| Playback analytics | POST `/analytics/playback/` |

## Important note about existing frontend paths

The original frontend has convenience services named `showService`, `animeService`, and `userService`. The backend exposes the content catalog through `/movies/` with `content_type=show` or `content_type=anime`, and the authenticated profile through `/auth/me/`. If desired, the frontend service layer should point those calls to the corresponding backend filters.
