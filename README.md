# django-admin-styles

An iOS-inspired skin for Django Admin (`iosadmin`).

Repository: [mrsnurk32/django-admin-styles](https://github.com/mrsnurk32/django-admin-styles)

It keeps every Django admin view and widget intact — changelists, filters,
inlines, actions, history, delete confirmations — and restyles them to feel
like Settings on iPhone: grouped lists, large titles, system blue, frosted
navigation, and light/dark mode.

## Features

- Drop-in install: add the app **above** `django.contrib.admin`
- Light and dark themes that follow Django’s built-in theme toggle
- Cupertino color tokens (system blue, grouped backgrounds, hairline separators)
- Frosted navigation bar and sticky save toolbar
- Settings-style sidebar and dashboard cards
- iOS-like login screen
- Accent color and app-icon glyph configurable from `settings.py`

## Requirements

- Python 3.10+
- Django 4.2+ (tested against Django 6.1)

## Install

```bash
pip install -e git+https://github.com/mrsnurk32/django-admin-styles.git#egg=django-iosadmin
```

Or copy the `src/iosadmin` package into your project.

## Setup

```python
# settings.py

INSTALLED_APPS = [
    "iosadmin",          # before django.contrib.admin
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "iosadmin.context_processors.iosadmin",
            ],
        },
    },
]
```

Collect static files in production:

```bash
python manage.py collectstatic
```

## Configuration

All keys are optional.

```python
IOSADMIN = {
    "ACCENT": "#007AFF",       # iOS system blue
    "ACCENT_DARK": "#0A84FF",  # iOS system blue (dark)
    "SITE_MARK": "A",          # letter inside the app icon
    "LARGE_TITLES": True,      # 34pt page titles
    "SHOW_APP_ICON": True,
}

ADMIN_SITE_HEADER = "Studio"
ADMIN_SITE_TITLE = "Studio Admin"
ADMIN_INDEX_TITLE = "Library"
```

If `SITE_MARK` is omitted, the first letter of `ADMIN_SITE_HEADER` is used.

## How it works

`iosadmin` ships two template overrides:

- `admin/base_site.html` — injects the stylesheet, script, branding, and CSS variables
- `admin/login.html` — iOS-style sign-in card

Everything else is CSS layered on top of Django’s own markup and CSS variables
(`--primary`, `--body-bg`, `--link-fg`, …). Your `ModelAdmin` classes do not
need to change.

## Demo

```bash
cd demo
python -m venv .venv
source .venv/bin/activate
pip install django
pip install -e ..
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/admin/

## Customizing further

Add project-level `templates/admin/base_site.html` that extends
`admin/base.html` if you need extra blocks, or append CSS after iosadmin’s
sheet via `{% block extrastyle %}`.

To change only the accent without a settings dict, override `--ios-accent`
in your own stylesheet.

## Limitations

- Wide changelist tables still scroll horizontally on small phones
- Tabular inlines are denser than stacked inlines; prefer stacked on mobile-first admins
- This is a visual layer, not a replacement for Unfold-style extra widgets

## License

MIT
