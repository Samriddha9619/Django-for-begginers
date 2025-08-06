from django.test import SimpleTestCase

class Testhomepage(SimpleTestCase):
    def test_urlhome(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
class Testaboutpage(SimpleTestCase):
    def test_urlabout(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
        