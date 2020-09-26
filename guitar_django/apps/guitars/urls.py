from django.urls import path

from . import views

app_name = 'guitars'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:guitar_id>/', views.detail, name = 'detail'),
    path('<int:guitar_id>/leave_comment/', views.leave_comment, name = 'leave_comment')
]