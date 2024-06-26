from django.views.generic import TemplateView
from . import models
from django.views import generic

from .models import Slogan


class HomePageView(generic.ListView):
    template_name = 'main/home.html'
    context_object_name = 'main_menu_list'
    model = models.Slogan
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slogans'] = models.Slogan.objects.order_by('-id')
        context['top_products'] = models.TopProduct.objects.order_by('-id')[:5]
        context['youtube_videos'] = models.YouTubeVideo.objects.order_by('-id')[:5]
        return context
