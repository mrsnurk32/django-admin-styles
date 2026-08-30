from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=80, blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Album(models.Model):
    class Format(models.TextChoices):
        DIGITAL = "digital", "Digital"
        VINYL = "vinyl", "Vinyl"
        CD = "cd", "CD"

    title = models.CharField(max_length=160)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    released = models.DateField(null=True, blank=True)
    format = models.CharField(max_length=16, choices=Format.choices, default=Format.DIGITAL)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=9.99)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-released", "title"]

    def __str__(self):
        return self.title


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="tracks")
    number = models.PositiveSmallIntegerField(default=1)
    title = models.CharField(max_length=160)
    duration_seconds = models.PositiveIntegerField(default=180)

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.number}. {self.title}"
