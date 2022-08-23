from django.views.generic import TemplateView
# typically, templates are written in HTML

# class in charge of showing homepage
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

