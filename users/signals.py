from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import logging

logging.basicConfig(level=logging.DEBUG)


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance

        profile = Profile.objects.create(
            user=user,
            username = user.username,
            email = user.email,
            name= user.first_name
        )

        logging.info("New Profile has been created")
    else:
        logging.info("User profile already exists")

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    logging.warn("User has been deleted")

post_delete.connect(deleteUser, sender=Profile)
# post_save.connect(createProfile, sender=User)