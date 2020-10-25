from django.contrib import admin
from .models import Category, Photo # models.py-ból a Category osztály beimportja


admin.site.register(Category) # a Category osztály kezelése jelenjen meg az admin oldalon

class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "uploaded", "image"] # admn felületen a megjelenő oszlopok
    list_editable = ["category"] # belelépés nélkül is tudja módosítani
    search_fields = ["title"] # title-re lehessen keresni
    list_filter = ["category"]


admin.site.register(Photo, PhotoAdmin) # a Photo osztály kezelése jelenjen meg az admin oldalon. PhotoAdmin oszlopok is jelenjenek meg


# settings.py-ban gallery app hozzáadása
"""adatmodel létrehozása, ..., migrálás"""
""" migrálás parancssorban manage.py makemigrations és manage.py migrate"""


