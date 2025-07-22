from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from moods.models import MoodEntry
from .models import Review
from datetime import date
from django.db.models import Count, Avg
# Create your views here.

def home_view(request):
    recent_entries = MoodEntry.objects.order_by('-created_at')[:6]
    reviews = Review.objects.order_by('-created_at')[:4]

    mood_stats = MoodEntry.objects.values('mood').annotate(count=Count('mood'))
    total_moods = sum(item['count'] for item in mood_stats)
    most_common_mood = max(mood_stats, key=lambda x: x['count']) if mood_stats else {'mood': 'N/A', 'count': 0}
    mood_percentage = int((most_common_mood['count'] / total_moods) * 100) if total_moods else 0

    # for avg rating
    average_rating = Review.objects.aggregate(avg=Avg('rating'))['avg']
    average_rating = round(average_rating or 0, 1)

    return render(request, 'main/home.html', {
        'recent_entries': recent_entries,
        'reviews': reviews,
        'most_common_mood': most_common_mood['mood'],
        'mood_percentage': mood_percentage,
        'total_moods': total_moods,
        'average_rating': average_rating,
        'total_reviews': Review.objects.count(),
    })