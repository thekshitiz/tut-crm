from django.db import models

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
    

    def __str__(self):
      return(f"{self.full_name} {self.email} ")
