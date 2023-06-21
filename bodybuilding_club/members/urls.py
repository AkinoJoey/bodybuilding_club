from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('rules/', views.rules, name="rules"),
    path('members/', views.members, name="members"),
    path('members/details/<int:id>', views.details, name="details"),
    path('testing/', views.testing, name='testing'),
]