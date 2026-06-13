# Deployment

## Static Assets Pipeline

Assets are built from `{{ cookiecutter.project_name }}/static/src/` and output to `{{ cookiecutter.project_name }}/static/public/`.

```
docs/static/src/
├── css/
│   ├── source.css      # Tailwind v4 entry point (imports basecoat + theme)
│   ├── basecoat.css     # Basecoat design system components
│   └── theme.css        # Project color palette (light + dark)
└── js/
    ├── app.js           # App entry point (imports vendors via esbuild)
    └── vendors/         # Vendor JS (basecoat, dropdown-menu, etc.)
```

### Build commands

| Command | Description |
|---------|-------------|
| `just tailwind-install` | Download Tailwind CLI binary |
| `just tailwind-build` | Build CSS → `static/public/css/styles.css` |
| `just tailwind-watch` | Watch CSS for changes (dev) |
| `just esbuild-install` | Download esbuild binary |
| `just js-build` | Bundle JS → `static/public/js/app.js` |
| `just js-watch` | Watch JS for changes (dev) |
| `just static-build` | Build all assets (CSS + JS) |
| `just collectstatic` | Build assets + run `collectstatic` |

### Development

The `Procfile.dev` starts both watchers:

```
web: just dj runserver 8000
js: just js-watch
tailwind: just tailwind-watch
worker: just dj db_worker -v 3
```

Run with `uvx honcho -f Procfile.dev start`.

### Production

`just collectstatic` handles the full pipeline:

1. `just static-build` — bundles JS with esbuild, compiles CSS with Tailwind
2. `dj collectstatic` — copies built assets to `STATIC_ROOT` with versioned hashes

### Why esbuild instead of django-compressor?

Django-compressor was replaced by a simpler approach:

- **esbuild** bundles JavaScript at build time (not runtime), producing minified output with sourcemaps
- **Whitenoise** (`CompressedManifestStaticFilesStorage`) handles compression, caching, and serving at runtime
- No runtime overhead, no template tag soup, no extra middleware

## Serving

[Whitenoise](https://whitenoise.readthedocs.io/) serves all static files in production:

```python
# settings.py
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
```

- Integrates with Django's `STATIC_ROOT` and `STATIC_URL`
- Adds `Cache-Control` headers for immutable files (hashed filenames)
- Gzip/Brotli compresses on the fly
- No nginx/apache dependency for static files

## Deployment Options

### 1. Docker (recommended)

A `deploy/Dockerfile` builds a production image:

```
docker build -t {{ cookiecutter.project_name }}:latest -f deploy/Dockerfile .
docker run -e DATABASE_URL=... -e SECRET_KEY=... {{ cookiecutter.project_name }}:latest
```

The image runs `just collectstatic` during build and serves with `daphne` + Whitenoise.

### 2. CapRover

The `.github/workflows/cd.yml` workflow builds and deploys to CapRover:

1. Builds Docker image
2. Pushes to CapRover registry
3. Triggers CapRover deploy via webhook

Configuration via repository secrets:
- `CAPROVER_URL`
- `CAPROVER_PASSWORD`
- `CAPROVER_APP_NAME`

### 3. Binary distribution (pyapp)

Build a self-contained binary with `just build-bin`:

```
just build-bin
./dist/{{ cookiecutter.project_name }}-<version>
```

This bundles Python + app into a single executable. Useful for minimal VMs or edge deployments.

### 4. Platform-as-a-Service

Any WSGI/ASGI-compatible platform works:

- **Railway** — set `DJANGO_SETTINGS_MODULE` and run `just dj migrate && daphne {{ cookiecutter.project_name }}.asgi:application`
- **Fly.io** — use the included Dockerfile
- **Heroku** — add a `Procfile` with `web: daphne {{ cookiecutter.project_name }}.asgi:application`

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DATABASE_URL` | Yes | — | Database connection string |
| `SECRET_KEY` | Yes | — | Django secret key |
| `DEBUG` | No | `False` | Enable debug mode |
| `ALLOWED_HOSTS` | No | `["localhost"]` | Comma-separated hosts |
| `ADMIN_URL` | No | `"admin/"` | Admin URL path |
| `CACHE_LOCATION` | No | `.diskcache` | Cache directory |
| `SENTRY_DSN` | No | — | Sentry DSN for error tracking |
| `CSRF_COOKIE_SECURE` | No | `True` (prod) | Secure CSRF cookie |
| `AWS_ACCESS_KEY_ID` | No* | — | S3 access key |
| `AWS_SECRET_ACCESS_KEY` | No* | — | S3 secret key |
| `AWS_STORAGE_BUCKET_NAME` | No* | — | S3 bucket name |
| `AWS_S3_REGION_NAME` | No* | — | S3 region |

*Required only when `USE_S3=True` and in production.

## Health Check

The `/health/` endpoint returns:

```json
{
  "status": "healthy",
  "checks": {
    "database": "ok",
    "cache": "ok"
  }
}
```

Configure your load balancer or monitoring to hit this endpoint.
