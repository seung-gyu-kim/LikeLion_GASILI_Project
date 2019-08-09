from django.urls import path
from . import views

urlpatterns = [
    path('servicecenter/', views.servicecenter, name='servicecenter'),
    
]
