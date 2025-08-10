from django.test import SimpleTestCase

# Create your tests here.
from django.urls import reverse

class HomePageTests(SimpleTestCase):
    def test_url_correct(self):
        res=self.client.get("/")
        self.assertEqual(res.status_code,200)

    def test_homepage(self):
        res= self.client.get(reverse("home"))
        self.assertEqual(res.status_code,200)
        self.assertTemplateUsed(res,"home.html")
        self.assertContains(res,"Home")