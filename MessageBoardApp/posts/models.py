from django.db import models

# Create your models here.
class AboutPost(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address= models.CharField(max_length = 50)
    phone = models.IntegerField()
    note = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name, 
