from django.conf.urls import path, include
from . import views

#/products/1/detail
#/products/new

urlpatterns = [
    path('index/', views.index, name='index'),
    path('another_example/', views.another_example_view),
]