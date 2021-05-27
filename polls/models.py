from django.db import models
from django.db import models
import os
from django.db.models.fields import CharField
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token
# Create your models here.
GENDER_CHOICES = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE')
)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Regionss(models.Model):
    RegionCode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
         return self.name

class Districts(models.Model):
    name = models.CharField(max_length=20 ,default="none")
    districtsCode = models.IntegerField(primary_key=True)
    Regions = models.ForeignKey(Regionss,on_delete=models.CASCADE)

    def __str__(self):
         return self.name

class Wards(models.Model):
      name = models.CharField(max_length=20)
      WardCode = models.IntegerField(primary_key=True)
      Council = models.ForeignKey(Districts,on_delete=models.CASCADE)

      def __str__(self):
            return self.name



class User(AbstractUser):
   middle_name = models.CharField(max_length=20, blank=True)
   date_of_birth = models.DateField(null=True)
   phone_number =models.CharField(max_length=20)
   Nationality= models.CharField(max_length=20,null=True)
   Region = models.ForeignKey(Regionss,on_delete=models.CASCADE,null=True)
   gender = models.CharField(max_length=10,null=True,choices=GENDER_CHOICES )
   created_at = models.DateTimeField(default=timezone.now)
   updated_at = models.DateTimeField(default=timezone.now)
   phone_number= models.CharField(max_length=15,blank=True)

def news(instance, filename):
    ext = filename.split('.')[-1]  # Get file extension

    if instance.pk:  # Get filename
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join('newsletters', filename)

class Newsletter(models.Model):
   title = models.CharField(max_length=20)
   description = models.CharField(max_length=20)
   src = models.FileField(upload_to=news,null=True, blank=True)

def videos(instance, filename):
    ext = filename.split('.')[-1]  # Get file extension

    if instance.pk:  # Get filename
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join('videos', filename)

class Video(models.Model):
   title = models.CharField(max_length=20)
   description = models.CharField(max_length=20)
   src = models.FileField(upload_to=videos,null=True, blank=True)   

def article(instance, filename):
    ext = filename.split('.')[-1]  # Get file extension

    if instance.pk:  # Get filename
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join('article', filename)




class Article(models.Model):
   title = models.CharField(max_length=20)
   description = models.CharField(max_length=20)
   src = models.FileField(upload_to=article,null=True, blank=True)     