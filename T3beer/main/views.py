from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from moods.models import MoodEntry
from .models import Review
from datetime import date
from django.db.models import Count, Avg
from .models import Post
import random
from django.core.paginator import Paginator
from .forms import PostForm
from django.db.models import Q
from .forms import ReviewForm
from django.contrib import messages
from .models import Game
from .forms import ContactForm
# Create your views here.

def home_view(request):
    # #did not render this..just testing
    # recent_entries = MoodEntry.objects.order_by('-created_at')[:6]
    # mood_stats = MoodEntry.objects.values('mood').annotate(count=Count('mood'))
    # total_moods = sum(item['count'] for item in mood_stats)
    # most_common_mood = max(mood_stats, key=lambda x: x['count']) if mood_stats else {'mood': 'N/A', 'count': 0}
    # mood_percentage = int((most_common_mood['count'] / total_moods) * 100) if total_moods else 0

    # # for avg rating
    # average_rating = Review.objects.aggregate(avg=Avg('rating'))['avg']
    # average_rating = round(average_rating or 0, 1)
    
    # for my reviews section
    reviews = Review.objects.order_by('-created_at')[:4]
    
    posts = list(Post.objects.all())
    random.shuffle(posts)
    random_posts = posts[:6]

    return render(request, 'main/home.html', {
        # 'recent_entries': recent_entries,
         'reviews': reviews,
        # 'most_common_mood': most_common_mood['mood'],
        # 'mood_percentage': mood_percentage,
        # 'total_moods': total_moods,
        # 'average_rating': average_rating,
        # 'total_reviews': Review.objects.count(),
        'posts': random_posts,
    })
    

def all_posts_view(request):
    posts = Post.objects.all()

    # my filter based on catagories
    category = request.GET.get('category')
    if category and category != 'All':
        posts = posts.filter(category=category)

    # search field
    search_query = request.GET.get('search')
    if search_query:
        posts = posts.filter(title__icontains=search_query)

    # Pagination to see pages order
    paginator = Paginator(posts.order_by('-created_at'), 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'posts': posts,
        'category': category or 'All',
        'search_query': search_query or '',
        'categories': ['All'] + [c[0] for c in Post.CATEGORY_CHOICES],
    }
    return render(request, 'main/posts.html', context)


def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('main:all_posts')
    return render(request, 'main/update_post.html', {'form': form})

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        return redirect('main:all_posts')
    return render(request, 'main/delete_post.html', {'post': post})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:all_posts')  
    else:
        form = PostForm()
    
    return render(request, 'main/add_post.html', {'form': form})


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("""
                <script>
                    alert("Review submitted successfully!");
                    window.location.href = "/";
                </script>
            """)
    else:
        form = ReviewForm()

    return render(request, 'main/add_review.html', {'form': form})


def games_list(request):
    search_query = request.GET.get('search', '')
    games = Game.objects.all()

    if search_query:
        games = games.filter(
            Q(name__icontains=search_query) |
            Q(category__icontains=search_query)
        )

    paginator = Paginator(games, 6)  
    page_number = request.GET.get('page')
    games_page = paginator.get_page(page_number)

    return render(request, 'main/games.html', {
        'games': games_page,
        'search_query': search_query
    })
    


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/contact_success.html')  
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def about_view(request):
    return render(request, 'main/about.html')
