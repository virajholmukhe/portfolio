from django.contrib import admin
from .models import Contact, ContactMe, Profile,Languages, Project

class ProfileAdmin(admin.ModelAdmin):
    list_display=('id','name','about','image')
admin.site.register(Profile,ProfileAdmin)

class LanguageAdmin(admin.ModelAdmin):
    list_display=('id','name','knowledge')
admin.site.register(Languages,LanguageAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display=('id','name','about','image','url','repo')
admin.site.register(Project,ProjectAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','email','phone','address')
admin.site.register(Contact,ContactAdmin)

class ContactMeAdmin(admin.ModelAdmin):
    list_display=('id','name','email','subject','message')
admin.site.register(ContactMe,ContactMeAdmin)