from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Urldetail
import datetime


@receiver(pre_save, sender=Urldetail)
def TimeUpdateSignal(sender, instance, **kwargs):
    print(sender)
    instance.updated = datetime.datetime.now()
