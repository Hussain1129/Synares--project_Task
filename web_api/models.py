from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
# Create your models here.


class StudentModel(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]

    def __str__(self):
        return self.username


class WebUrl(models.Model):
    urlname = models.URLField(max_length=200)

    def __str__(self):
        return self.urlname


class Urldetail(models.Model):
    weburls = models.OneToOneField(WebUrl, on_delete=models.CASCADE)
    counts = models.IntegerField(default=1)
    userurl = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    updated = models.DateTimeField(default=None)

    # def __str__(self):
    #     return f'{self.weburls}----{self.counts}----{self.updated}'
