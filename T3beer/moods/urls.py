from django.urls import path
from . import views

app_name = "moods"

urlpatterns = [

    path('express/', views.express_mood, name='express'),
    path('result/<int:id>/', views.mood_result, name='result'),  
]