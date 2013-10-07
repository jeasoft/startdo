from users.models import Industry, Skill, UserProfile
from django.contrib import admin

class IndustryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

class SkillAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(UserProfile)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(Skill, SkillAdmin)
