from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    context={
        "inventory":["widgets1","widgets2","widgets3"],
        "greetings": "ThanKYOU For VISIting ",
    }
    return render(request,"home.html",context)

class AboutView(TemplateView):
    template_name="about.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["Contact_add"]="Delhi NCR"
        context["phone_no"]= 123456790
        return context
