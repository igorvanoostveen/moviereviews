from django.shortcuts import render

from .models import Newsitem

def news(request):
    news = Newsitem.objects.all().order_by('-date')
    
    return render(request, 'news.html', {'news': news})
