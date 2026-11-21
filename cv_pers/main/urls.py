from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history/people/', views.history_people, name='history_people'),
    path('history/photos/', views.history_photos, name='history_photos'),
    path('history/', views.history, name='history'),
    path('history/<path:subpath>', views.history),
    path('news/', views.news, name='news'),
    path('news/<path:subpath>', views.news),
    path('management/', views.management, name='management'),
    path('management/<path:subpath>', views.management),
    path('facts/', views.facts, name='facts'),
    path('facts/<path:subpath>', views.facts),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<path:subpath>', views.contacts),

]