import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_mood(text):
    scores = sia.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.5:
        return "Happy"
    elif compound <= -0.5:
        return "Sad"
    else:
        return "Neutral"



