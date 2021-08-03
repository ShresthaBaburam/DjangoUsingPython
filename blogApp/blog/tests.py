from django.test import TestCase,Client 
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Posts

# Create your tests here.

def setUp(self):
    self.user= get_user_model().objects.create_user(
        username = 'testuser',
        email = 'test@email.com',
        password='secret',

    )
    self.post =Posts.objects.create(
        title = ' a good man',
        body='nice body hete',
        author=self.user,
    )
def test_string_representaion(self):
    post = Posts(title=' a good man')
    self.assertEqual(str(post),post.title)

def test_post_content(self):
    self.assertEqual(f'{self.post.title}','a good man')
    self.assertEqual(f'{self.post.author}','testuser')
    self.assertEqual(f'{self.post.body}','nice body hete')

def test_post_list_content(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response,'nice body hete')
    self.assertTemplateUsed(response,'home.html')

def test_post_detail_content(self):
    response = self.client.get('/post/1/')
    no_response = self.client.get('/post/100000/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)
    self.assertContains(response,'a good man')
    self.assertTemplateUsed(response,'post_detail.html')