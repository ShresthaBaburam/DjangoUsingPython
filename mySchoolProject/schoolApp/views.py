from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, CreateView, DeleteView,UpdateView
from .models import *
from .login import StudentLogin
from .register import StudentRegisterForm
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class CoursePageView(TemplateView):
    template_name = 'course.html'

class EventPageView(TemplateView):
    template_name = 'event.html'

class ServicePageView(TemplateView):
    template_name = 'service.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class JoinPageView(TemplateView):
    template_name = 'join.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'
    form_class = StudentLogin
    success_url= reverse_lazy('student_page')

class RegisterPageView(CreateView):
    template_name = 'register.html'
    form_class = StudentRegisterForm
    success_url = reverse_lazy('login')
    

    
