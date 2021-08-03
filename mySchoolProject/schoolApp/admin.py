from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Course,Event,Service,About,Contact,Subscription,Register])

