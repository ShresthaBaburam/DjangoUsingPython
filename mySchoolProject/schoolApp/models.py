from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(auto_now_add = True, null=True,blank=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    def delete(self):
        pass
    
class Register(User):
    is_student = models.BooleanField(default=False)

    class Meta:
        verbose_name = ('Student')
        verbose_name_plural = ('Students')
        
    def __str__(self):
        return self.username

class Course(DateTimeModel):
    courseName = models.CharField(max_length=250)
    coureseBy = models.CharField(max_length=250)
    CourseDescription = models.TextField()
    courseImage = models.ImageField()

class Event(DateTimeModel):
    eventTitle =models.CharField(max_length=250)
    eventDescription =models.TextField()
    eventBy =models.CharField(max_length=250)
    eventAt = models.DateTimeField()

class Service(DateTimeModel):
    serviceTitile=models.CharField(max_length=250)
    serviceDescription = models.TextField()

class About(DateTimeModel):
    aboutTitle = models.CharField(max_length=250)
    aboutDexcription1=models.TextField()
    aboutDexcription2=models.TextField()


class Contact(DateTimeModel):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message =models.TextField()

class Subscription(DateTimeModel):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    message = models.TextField()


