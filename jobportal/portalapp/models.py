from django.db import models
# from django.contrib.auth.models import User

from django.contrib.auth.models import User


# Create your models here.



class usermodel(models.Model): #jobseaker model
    username=models.CharField(max_length=100)
    email=models.EmailField()
    mob=models.IntegerField()
    dob=models.DateField()
    qualification=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


class profile1(models.Model): #company model
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    auth_token = models.CharField(max_length = 100)
    is_verified = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)



class Jobmodel(models.Model):
    cname = models.CharField(max_length=100)
    cemail = models.EmailField()
    ctitle = models.CharField(max_length=100)
    ctype = models.CharField(max_length=100)
    cexp = models.CharField(max_length=100)
    jtype = models.CharField(max_length=100)


class applyjob(models.Model):
    exp = [
        ('0-1', '0-1'),
        ('1-2', '1-2'),
        ('2-3', '2-3'),
        ('3-4', '3-4'),
        ('4-5', '4-5'),
        ('5-6', '5-6'),
        ('6-7', '6-7'),
        ('7-8', '7-8')
    ]
    cname = models.CharField(max_length=100)
    jtitle = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    quali = models.CharField(max_length=100)
    phone = models.IntegerField()
    uexp = models.CharField(max_length=30,choices=exp)
    resume = models.ImageField(upload_to='portalapp/static')


