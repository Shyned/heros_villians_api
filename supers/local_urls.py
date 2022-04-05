from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_super_list),
    path('<int:pk>/', views.change_super),
]