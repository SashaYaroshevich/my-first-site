from django.urls import path

from . import views

app_name = 'info'
urlpatterns = [
    path('', views.index, name='info'),
    path('wish/', views.wishs, name='wishs'),
    path('create/', views.create, name='create')
]