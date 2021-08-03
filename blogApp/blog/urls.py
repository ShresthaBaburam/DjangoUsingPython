from django.urls import path

from .views import HomePageView,DetailPageView

urlpatterns=[
    
    path('', HomePageView.as_view(), name= 'home'),
    path('post/<str:pk>/',DetailPageView.as_view(),name='post_detail'),

]