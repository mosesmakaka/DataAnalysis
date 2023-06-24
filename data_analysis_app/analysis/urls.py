from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Add this line for the root URL
    path('analysis/', views.analyze_data, name='analyze_data'),
    # Other URL patterns for your application
]
