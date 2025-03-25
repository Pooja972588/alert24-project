from django.shortcuts import render
from app .models import Categories, News


def search(request):
    query = request.GET.get('search')
    data = News.objects.filter(title__icontains = query)
    context = {
        'news': data
    }
    return render(request, "categories/search.html", context)



def home(request):
    categry = Categories.objects.all()
    allNews = News.objects.all().order_by('-id')
    topNews = News.objects.all().order_by('id')[:5]
    context = {
        'categories': categry,
         'allNews': allNews,
         'topNews': topNews
         }
    return render (request, "index.html", context )
 
def india(request):
    categry = Categories.objects.all()
    allNews = News.objects.filter(category__title ='India News').order_by('-id')
    topNews = News.objects.all().order_by('id')[:5]
    context = {
        'categories': categry,
         'allNews': allNews,
         'topNews': topNews
         }
    return render (request, 'categories/india.html', context)

def bollywood(request):
    categry = Categories.objects.all()
    allNews = News.objects.filter(category__title ='Bollywood News').order_by('-id')
    topNews = News.objects.all().order_by('id')[:5]
    context = {
        'categories': categry,
         'allNews': allNews,
         'topNews': topNews
         }
    return render(request, "categories/bollywood.html", context)

def sport(request):
    categry = Categories.objects.all()
    allNews = News.objects.filter(category__title ='Sport News').order_by('-id')
    topNews = News.objects.all().order_by('id')[:5]
    context = {
        'categories': categry,
         'allNews': allNews,
         'topNews': topNews
         }
    return render(request, 'categories/sport.html', context)

def health(request):
    categry = Categories.objects.all()
    allNews = News.objects.filter(category__title = 'Health News').order_by('-id')
    topNews = News.objects.all().order_by('id')[:5]
    context = {
        'categories': categry,
         'allNews': allNews,
         'topNews': topNews
         }
    return render(request, 'categories/health.html', context)

def details(request, id):
    news_details = News.objects.get( pk = id )
    topNews = News.objects.all().order_by('id')[:5]
    categry = Categories.objects.all()
    context = {
        'news': news_details,
        'categories': categry,
         'topNews': topNews
    }
    return render(request, "details.html", context)
