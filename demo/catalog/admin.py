from django.contrib import admin

from .models import Album, Artist, Track


class TrackInline(admin.TabularInline):
    model = Track
    extra = 1


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "is_featured")
    list_filter = ("is_featured", "country")
    search_fields = ("name", "country")


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "released", "format", "price")
    list_filter = ("format", "released")
    search_fields = ("title", "artist__name")
    autocomplete_fields = ("artist",)
    inlines = [TrackInline]
    fieldsets = (
        (None, {"fields": ("title", "artist", "released")}),
        ("Store", {"fields": ("format", "price")}),
        ("Notes", {"fields": ("notes",), "classes": ("collapse",)}),
    )
