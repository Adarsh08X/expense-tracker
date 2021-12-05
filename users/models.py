from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#Logger
import logging
logger = logging.getLogger(__name__)

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    income = models.FloatField(default=0)
    expenses = models.FloatField(default=0)
    balance = models.FloatField(default=0)

    def __str__(self):
        return str(self.user)

def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
        logger.error("Profile Created!")


post_save.connect(create_profile, sender=User)
        
