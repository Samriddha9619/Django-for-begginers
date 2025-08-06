from django.test import SimpleTestCase
from django.urls import reverse
class Testhome(SimpleTestCase):
    def test_urlhome(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code,200)
    def test_byname_home(self):
        response =self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
    def test_templatename_correct(self):
        response =self.client.get(reverse("home"))
        self.assertTemplateUsed(response,"home.html")
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Company Homepage</h1>")


class Testabout(SimpleTestCase):
    def test_urlabout(self):
        response=self.client.get("/about/")
        self.assertEqual(response.status_code,200)
    def test_byname_about(self):
        response =self.client.get(reverse("about"))
        self.assertEqual(response.status_code,200)
    def test_templatename_correct(self):
        response =self.client.get(reverse("about"))
        self.assertTemplateUsed(response,"about.html")
    def test_template_content(self):
        response =self.client.get(reverse("about"))
        self.assertContains(response, "<h1>Company about page</h1>")
