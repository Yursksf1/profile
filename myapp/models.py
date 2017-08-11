# models.py 
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
#from mezzanine.core.fields import FileField
from django.db.models.signals import post_save


MUNICIPIO = (
    ("B", "Bucaramanga"),
    ("G", "Girón"),
    ("F", "Floridablanca"),
    ("P", "Piedecuesta"),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    #photo = FileField(verbose_name=_("Profile Picture"),
    #                  upload_to=upload_to("main.UserProfile.photo", "profiles"),
    #                  format="Image", max_length=255, null=True, blank=True)
    numDoc = models.CharField("Numero de Documento",max_length=20, blank=True)
    firsrtName = models.CharField("Nombres" ,max_length=300, blank=True)
    lastName = models.CharField("Apellidos" ,max_length=300, blank=True)

    phone = models.CharField("Número de Teléfono",max_length=20, blank=True)
    municipality = models.CharField("Municipio de Residencia",max_length=1, choices=MUNICIPIO, blank=True)
    address = models.CharField("Dirección Residencia" ,max_length=100,  blank=True)

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)
