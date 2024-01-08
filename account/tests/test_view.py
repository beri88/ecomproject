from django.test import TestCase,Client
from django.urls import reverse


class TestView(TestCase):
    def testviewhome(self):
        clientdemo=Client()
        response_home=clientdemo.get(reverse('home'))
        print("Response",response_home)
        self.assertEquals(response_home.status_code,200)
        self.assertTemplateUsed(response_home,'home.html')
        
