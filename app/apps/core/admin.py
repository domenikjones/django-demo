from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):

    change_list_template = "admin/change_list_filter_sidebar.html"
