from django.contrib import admin
from django.urls import path

admin.site.site_header = "Studio"
admin.site.site_title = "Studio Admin"
admin.site.index_title = "Library"

urlpatterns = [
    path("admin/", admin.site.urls),
]
