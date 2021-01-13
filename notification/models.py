from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.urls import reverse
from PIL import Image

# Create your models here.



class Notification(models.Model):
    title= models.CharField(max_length=255)
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('notification:show', args=[self.id])
        

@receiver(post_save ,sender=User)
def create_welcome_message(sender , **kwargs):
    if kwargs.get('created' , False):
        Notification.objects.create(user=kwargs.get('instance'),
                                    title="welcome to our Django site",
                                    message = "Thank you signing up !")

