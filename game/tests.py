from django.test import TestCase, Client

class MyTest(TestCase):
    def setUp(self):
        print('running a test')
        self.client = Client()
