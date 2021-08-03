

from .models import Posts
from django.views.generic import ListView, DetailView


# Create your views here.

class HomePageView(ListView):
    model = Posts
    template_name = 'home.html'


class DetailPageView(DetailView):
    model = Posts
    template_name = 'post_detail.html'