from django.test import SimpleTestCase


# Create your tests here.
class SimpleTests(SimpleTestCase):
    def testHomePageView(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def testAboutPageView(self):
        response = self.client.get('about/')
        self.assertEqual(response.status_code, 200) 
        
         
    def testContactPageView(self):
        response = self.client.get('contact/')
        self.assertEqual(response.status_code, 200)  