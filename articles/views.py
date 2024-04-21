from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'articles/home.html'
