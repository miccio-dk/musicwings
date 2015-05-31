from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from musicwings.apps.musicwings_ws.models import *


class AuthorInline(admin.StackedInline):
    model = Author
    can_delete = False
    verbose_name_plural = 'authors'

class UserAdmin(UserAdmin):
    inlines = (AuthorInline, )



class WorkInLine(admin.TabularInline):
    model = Work
    extra = 3

class StudyInLine(admin.TabularInline):
    model = Study
    extra = 3

class CVAdmin(admin.ModelAdmin):
    inlines = (WorkInLine, StudyInLine, )



admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(CV, CVAdmin)
admin.site.register(Employer)
admin.site.register(Institution)
admin.site.register(Job)
admin.site.register(Education)


