from rest_framework import routers
from django.urls import path, include

from Service import views
from Service.api_views import ArticleView

app_name = 'Service'

router = routers.DefaultRouter()
router.register('article', ArticleView)

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('latest-update', views.latest_update, name='latest-update'),
    path('admin-manager', views.admin, name='admin'),
    path('admin-manager/upload', views.upload, name='upload'),
    path('api/', include(router.urls)),
]


