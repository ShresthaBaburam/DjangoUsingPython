from django.shortcuts import render
from django.views.generic import ListView
from .models import AboutPost

# Create your views here.

class HomePageView(ListView):
    model = AboutPost
    template_name = 'home.html'


