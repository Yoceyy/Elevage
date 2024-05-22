from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    message = models.TextField(max_length=400, null=True)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phone} - {self.created}'
