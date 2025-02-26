from django.db import models
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def save(self, *args, **kwargs):
        if not self.id:  # New instance
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Client, self).save(*args, **kwargs)

    def __str__(self):
      return(f"{self.full_name} {self.email}")
