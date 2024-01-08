from django.test import TestCase,Client
from django.urls import reverse,resolve
#from .views import pro
from account .views import login_user
class TestUrl(TestCase):
    def testhome(self):
        response=self.client.get('/home/')
        print(response)
        self.assertEqual(response.status_code,200)

class testurl(TestCase):
    def testlogin(self):
        url=reverse('login')
        print("resolved url:",resolve(url))
        self.assertEqual(resolve(url).func,login_user)