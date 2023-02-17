from django.contrib import admin
from MYapp.models import Company
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','location','job1','salary','job2','salary2']
admin.site.register(Company,CompanyAdmin)
