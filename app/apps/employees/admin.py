from django.contrib import admin

from core.admin import BaseAdmin
from employees.models import Employee
from restaurants.admin import JobInlines


class EmployeeAdmin(BaseAdmin):

    list_display = ('active', 'full_name', 'professionality')
    list_display_links = ('full_name',)
    list_filter = ('active', 'professionality')
    search_fields = ('first_name', 'last_name')
    list_editable = ('active', 'professionality')
    readonly_fields = ('date_of_birth',)

    inlines = [JobInlines]

    fieldsets = (
        ('General', {
            'fields': (
                ('first_name', 'last_name'),
                ('active', 'professionality'),
                'date_of_birth',
            )
        }),
    )

    def full_name(self, obj):
        return obj.get_full_name()
    full_name.short_description = "Name"


admin.site.register(Employee, EmployeeAdmin)
