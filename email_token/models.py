from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User

# Create your models here.


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_token = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.email_token