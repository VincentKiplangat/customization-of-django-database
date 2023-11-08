from django.contrib import admin

from main_app.models import Employee

# Register your models here.
admin.site.site_header = "Roxs Collection"
admin.site.index_title = ("Roxs server"
                          "")


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', "dob", "disabled"]
    search_fields = ['name', 'email']
    list_filter = ["disabled"]


admin.site.register(Employee, EmployeeAdmin)
