from django.contrib import admin

from core.admin import BaseAdmin
from restaurants.models import Restaurant


class JobInlines(admin.TabularInline):

    model = Restaurant.employees.through
    extra = 0


class RestaurantAdmin(BaseAdmin):

    inlines = [JobInlines]


admin.site.register(Restaurant, RestaurantAdmin)
