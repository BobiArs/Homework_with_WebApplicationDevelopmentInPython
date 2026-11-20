from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('about', views.about, name='about'),
    path('card/<int:id>', views.get_card, name='card'),
    path('search', views.get_card_by_title, name='search'),
    path('create', views.create_card, name='create'),
    path('register/', views.register, name='register'),
    path('add/', views.add_card, name='add_card'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)