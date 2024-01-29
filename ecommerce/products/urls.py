from django.urls import path
from . import views


#products/1   products/new etc.

urlpatterns = [
    path('', views.index),
    path('new', views.new)

]
