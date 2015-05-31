from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from musicwings.apps.musicwings_ws.models import *


class MW_UserInline(admin.StackedInline):
	model = MW_User
	can_delete = False

class UserAdmin(UserAdmin):
	inlines = (MW_UserInline, )



class ContactInLine(admin.TabularInline):
	model = Contact
	extra = 3



admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Contact)
admin.site.register(ContactType)


