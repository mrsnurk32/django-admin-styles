from django.conf import settings

DEFAULTS = {
    "ACCENT": "#007AFF",
    "ACCENT_DARK": "#0A84FF",
    "SITE_MARK": "",
    "LARGE_TITLES": True,
    "SHOW_APP_ICON": True,
}


def get_iosadmin_settings():
    user = getattr(settings, "IOSADMIN", {}) or {}
    merged = {**DEFAULTS, **user}
    if not merged.get("SITE_MARK"):
        header = getattr(settings, "ADMIN_SITE_HEADER", None) or "Admin"
        merged["SITE_MARK"] = str(header).strip()[:1].upper() or "A"
    return merged
