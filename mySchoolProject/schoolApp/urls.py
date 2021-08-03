from django.urls import path
from .views import *
#app_name = 'school'
urlpatterns = [
    
    path('', HomePageView.as_view(), name= 'home'),
    path('course/', CoursePageView.as_view(), name= 'course'),
    path('event/', EventPageView.as_view(), name= 'event'),
    path('service/',ServicePageView.as_view(), name= 'service'),
    path('about/', AboutPageView.as_view(), name= 'about'),
    path('contact/', ContactPageView.as_view(), name= 'contact'),
    path('join/', JoinPageView.as_view(), name= 'join'),
    path('login/', LoginPageView.as_view(), name= 'login'),
    path('register/', RegisterPageView.as_view(), name= 'register'),
    
]