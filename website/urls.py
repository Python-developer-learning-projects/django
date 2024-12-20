from django.urls import path

from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('join', views.join, name='joins')
]