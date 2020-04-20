from django.urls import path
from . import views
urlpatterns = [
    path('', views.subscribe, name = 'subscribe'),
    path('mass', views.mass_email, name = "massemail")
]