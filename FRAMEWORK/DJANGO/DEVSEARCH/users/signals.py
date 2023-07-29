from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile
# Create your signals here.

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
def deleteuser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    


post_save.connect(createprofile, sender=User)
post_delete.connect(deleteuser, sender=Profile)