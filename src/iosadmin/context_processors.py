from .conf import get_iosadmin_settings


def iosadmin(request):
    return {"iosadmin": get_iosadmin_settings()}
