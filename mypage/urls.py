from django.urls import path
from . import views

urlpatterns = [
    path('mypageBlog/', views.mypageBlog, name='mypageBlog'),
    path('mypageComment/', views.mypageComment, name='mypageComment'),
]