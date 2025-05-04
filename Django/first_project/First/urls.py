from django.urls import path
from First  import views

urlpatterns = [
    path('', views.First, name='First')
]