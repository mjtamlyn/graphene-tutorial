from django.contrib import admin

from .models import House, Person, Street


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['street', 'number']
    list_filter = ['street']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'family', 'residence', 'spouse']
    list_filter = ['family', 'residence']
    filter_horizontal = ['parents']
