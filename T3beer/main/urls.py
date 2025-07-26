from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('posts/', views.all_posts_view, name='all_posts'),
    path('posts/update/<int:id>/', views.update_post, name='update_post'),
    path('posts/delete/<int:id>/', views.delete_post, name='delete_post'),
    path('posts/add/', views.add_post, name='add_post'),
    path('add-review/', views.add_review, name='add_review'),
    path('games/', views.games_list, name='games_list'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),
]