from django.db import models
from django.contrib.auth.models import User

class Contacts(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    contact_picture = models.URLField(null=True)
    is_favorite = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone_number}--{self.owner}"

    @property
    def owner_name(self):
        return self.owner.username

    @property
    def owner_email(self):
        return self.owner.email
