from .models import Post

sample_posts = [
    {
        "title": "Mindfulness Meditation for Anxiety",
        "excerpt": "Discover how practicing mindfulness can help you calm anxiety and stay present, even during tough moments.",
        "source": "Mindful.org",
        "link": "https://www.mindful.org/mindfulness-meditation-anxiety/",
        "category": "Mindfulness"
    },
    {
        "title": "Healthy Sleep and Mental Health",
        "excerpt": "Good sleep hygiene can transform your mental health. Learn habits that promote better sleep and reduce stress.",
        "source": "Healthline",
        "link": "https://www.healthline.com/health/healthy-sleep",
        "category": "Sleep"
    },
    {
        "title": "Use Your Five Senses to Calm Anxiety",
        "excerpt": "This grounding technique helps reduce anxiety by engaging all five senses to bring you back to the present.",
        "source": "PsychCentral",
        "link": "https://psychcentral.com/anxiety/using-the-five-senses-for-anxiety-relief",
        "category": "Anxiety"
    },
    {
    "title": "10 Grounding Techniques to Calm Anxiety",
    "excerpt": "When anxiety overwhelms you, grounding exercises can help bring you back to the present. Try these physical and mental techniques.",
    "source": "Healthline",
    "link": "https://www.healthline.com/health/grounding-techniques#physical-techniques",
    "category": "Anxiety"
    },
    {
        "title": "Breathwork for Emotional Balance",
        "excerpt": "Deep breathing can regulate stress responses. Explore how to integrate breathwork into your routine.",
        "source": "Verywell Mind",
        "link": "https://www.verywellmind.com/breathing-exercises-for-relaxation-2584115",
        "category": "Breathing"
    }
    
]

def run():
    for post in sample_posts:
        Post.objects.create(**post)
    print("Sample mental health posts added.")
