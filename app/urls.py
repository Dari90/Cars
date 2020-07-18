from app import views
from django.urls import path
from .views import CarList

app_name = 'app'
urlpatterns = [
    path('', views.CarList.as_view(), name='car-list'),
]
