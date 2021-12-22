from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from Service.models import Article


def home(request):
    return render(request, 'service/home.html')


def about(request):
    return render(request, 'service/about.html')


def contact(request):
    return render(request, 'service/contact.html')


def faq(request):
    return render(request, 'service/faq.html')


def latest_update(request):
    all_articles = Article.objects.all()
    return render(request, 'service/latest-update.html', {'all_articles': all_articles})


def admin(request):
    return render(request, 'service/admin.html')


def upload(request):
    topic = request.POST.get('topic')
    article = request.POST.get('article')
    image = request.FILES.get('image')
    date = timezone.now()
    Article.objects.create(topic=topic, article=article, image=image, date=date)
    messages.success(request, 'Article successfully uploaded')
    return HttpResponseRedirect(reverse('Service:admin'))


def error_400(request, exception):
    return render(request, 'service/400.html')


def error_403(request, exception):
    return render(request, 'service/403.html')


def error_404(request, exception):
    return render(request, 'service/404.html')


def error_500(request):
    return render(request, 'service/500.html')

