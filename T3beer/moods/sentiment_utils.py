import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from django.conf import settings
import os


sia = SentimentIntensityAnalyzer(os.path.join(settings.BASE_DIR, "moods/nltk_data/sentiment/vader_lexicon.txt"))

def analyze_mood(text):
    scores = sia.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.5:
        return "Happy"
    elif compound <= -0.5:
        return "Sad"
    else:
        return "Neutral"



