from django.shortcuts import render, redirect
from .forms import MoodEntryForm
from .models import MoodEntry
from nltk.sentiment import SentimentIntensityAnalyzer
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .sentiment_utils import analyze_mood

# Create your views here.


def express_mood(request):
    mood = None

    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            mood = analyze_mood(text)

            entry = form.save(commit=False)
            entry.mood = mood
            entry.save()
            return redirect('moods:result', entry.id)
    else:
        form = MoodEntryForm() 

    return render(request, 'moods/express.html', {'form': form})




def mood_result(request, id):
    entry = get_object_or_404(MoodEntry, id=id)
    mood = entry.mood

    #to see how many people felt the same today
    # today = timezone.now().date()
    # same_mood_count = MoodEntry.objects.filter(mood=mood, created_at__date=today).count()

    affirmations = {
        "Happy": "Keep shining! You’re a light in this world.",
        "Sad": "It's okay to feel sad — you're not alone.",
        "Neutral": "Steady days are powerful too.",
    }

    songs = {
        "Happy": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "Sad": "https://youtu.be/IQLLbTZ0tG0?si=eIQ5QIxU-slnbHtA",
        "Neutral": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    }

    return render(request, 'moods/result.html', {
        'entry': entry,
        #  'count': same_mood_count,
        'affirmation': affirmations.get(mood, ""),
        'song': songs.get(mood, "#"),
    })