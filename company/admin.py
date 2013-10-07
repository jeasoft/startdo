from django.contrib import admin
from company.models import Company, Category

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Company, CompanyAdmin)
admin.site.register(Category, CategoryAdmin)
