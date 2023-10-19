from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_ROLE=[(
        'Customer','Customer'
    ),
    ('Vendor','Vendor')]
    GENDER_CHOICES=[('Female','Female'),('Male','Male'),('Others','Others')]
    address=models.CharField(max_length=100)
    user_role=models.CharField(max_length=25,choices=USER_ROLE)
    gender=models.CharField(max_length=25,choices=GENDER_CHOICES)
    phone=models.IntegerField()
    email_verification_status=models.BooleanField(default=False)

class OtpVerificationModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_activation_keys")
    otp=models.CharField(max_length=50)

