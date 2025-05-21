from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
path('arie_naturala/<int:pk>/date_geografice/', views.date_geografice_detail, name='date_geografice_detail'),
path('arie_naturala/<int:pk>/date_hidrografice/', views.date_hidrografice_detail, name='date_hidrografice_detail'),
path('arie_naturala/<int:pk>/date_speologice/', views.date_speologice_detail, name='date_speologice_detail'),
path('arie_naturala/<int:pk>/date_forestiere/', views.date_forestiere_detail, name='date_forestiere_detail'),
path('arie_naturala/<int:pk>/date_biodiversitate/', views.date_biodiversitate_detail, name='date_biodiversitate_detail'),
path('discussions/', views.discussion_list, name='discussion_list'),
path('discussions/<int:discussion_id>/', views.discussion_detail, name='discussion_detail'),
path('discussions/new/', views.new_discussion, name='new_discussion'),
path('discussions/<int:discussion_id>/comment/', views.add_comment, name='add_comment'),
path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
path('discussions/<int:discussion_id>/delete/', views.delete_discussion, name='delete_discussion'),
path('chat/', views.chat, name='chat'),
path('send/', views.send_message, name='send_message'),
path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
path('petition/', views.petition_list, name='petition_list'),
path('petition/<int:petition_id>/', views.petition_detail, name='petition_detail'),
path('arii/', views.arii_naturale_list, name='arii_list'),
path('posts/', views.posts_list, name='posts_list'),

]