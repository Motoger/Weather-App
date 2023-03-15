from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_index/', views.new_index, name='new_index')
]