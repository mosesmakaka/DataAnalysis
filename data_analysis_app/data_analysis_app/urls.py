from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analysis/', views.analyze_data, name='analyze_data'),
    # Other URL patterns for your application
]
