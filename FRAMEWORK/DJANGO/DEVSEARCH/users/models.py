from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
import uuid
# Create your models here.

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True) 
    location = models.CharField(max_length=200, null=True, blank=True) 
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(blank=True, null=True,)
    profile_image = models.ImageField(null=True, blank=True, upload_to="profiles/", default="profiles/user-default.png")
    social_github = models.URLField(validators=[URLValidator(regex='https://github.com')], max_length=200, null=True, blank=True)
    social_linkedin = models.URLField(validators=[URLValidator(regex='https://www.linkedin.com')], max_length=200, null=True, blank=True)
    social_website = models.URLField(validators=[URLValidator(regex='https://')], max_length=200, null=True, blank=True)
    social_twitter = models.URLField(validators=[URLValidator(regex='https://twitter.com')], max_length=200, null=True, blank=True)
    social_youtube = models.URLField(validators=[URLValidator(regex='https://www.youtube.com')], max_length=200, null=True, blank=True)
    social_stackoverflow = models.URLField(validators=[URLValidator(regex='https://stackoverflow.com')], max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
    )
    
    def __str__(self):
        return str(self.username)

class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
    )
    
    def __str__(self):
        return str(self.name)
    
    
# @receiver(post_save, sender=Profile)
def createprofile(sender, instance, created, **kwergs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

# @receiver(post_delete, sender=Profile)
def deleteuser(sender, instance, **kwergs):
    user = instance.user
    user.delete()
    


# post_save.connect(createprofile, sender=User)
# post_delete.connect(deleteuser, sender=Profile)