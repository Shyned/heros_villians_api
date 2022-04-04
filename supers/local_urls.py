from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_super),
    path('<int:pk>/', views.get_super),
]