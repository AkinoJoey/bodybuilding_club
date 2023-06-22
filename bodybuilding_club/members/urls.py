from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('rules/', views.rules, name="rules"),
    path('notables/', views.notablesList, name="notables"),
    path('notables/<int:notablesIndex>', views.notablesDetail, name="notablesDetail"),
    path('externalLinks/', views.externalLinks, name="externalLinks"),
    path('testing/', views.testing, name='testing'),
]