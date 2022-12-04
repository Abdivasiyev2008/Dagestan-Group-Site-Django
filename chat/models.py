from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    is_login = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

class chatMessages(models.Model):
    user_from = models.ForeignKey(get_user_model(),
        on_delete=models.CASCADE,related_name="+")

    user_to = models.ForeignKey(get_user_model(),
        on_delete=models.CASCADE,related_name="+")

    message = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message
