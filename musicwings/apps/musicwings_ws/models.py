from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MW_User(models.Model):
	user			= models.OneToOneField(User)
	display_name	= models.TextField()

	class Meta:
        verbose_name = "MW User"
        verbose_name_plural = "MW Users"

	def __str__(self):
		return self.display_name

models.class ContactType(models.Model):
	descr		= models.TextField()

    class Meta:
        verbose_name = "Contact type"
        verbose_name_plural = "Contact types"

    def __str__(self):
        return self.descr
    

models.class Contact(models.Model):
	user 			= models.ForeignKey(MW_User)
	contact_type 	= models.ForeignKey(ContactType)
	contact_val		= models.TextField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.user.first_name
    