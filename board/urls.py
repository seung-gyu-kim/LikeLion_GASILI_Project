from django.urls import path
from . import views

urlpatterns = [
    path('new/',views.board_new, name="board_new"),
    path('create/',views.create, name="board_create"),
    path('test/<int:board_id>',views.test, name="test"),
    path('test/<int:board_id>/create/comment',views.createcomment, name="createcomment"),
    path('test/chart/<int:board_id>', views.chart, name='chart'),
    path('', views.board, name="board"),
]

