from django.shortcuts import render
from .models import Article
from django.http import HttpResponseNotFound

# Create your views here.
def latest(request):
    this_article = Article.objects.all().first()
    if this_article:
        context = {
            'heading':this_article.heading,
            'body' : this_article.body,
            'reporter' : this_article.reporter.name if this_article.reporter else '',
            'created' : this_article.created,
            'image' : this_article.image.url if this_article.image else None
        }
        return render(request, 'all.html', context)
    else:
        return HttpResponseNotFound("Article not found")

def article_details(request, pk):
    #pk =1
    ###print article_id
    # this_article = Article.objects.filter(id=pk).first()
    this_article = Article.objects.get(id=pk)
    if this_article:
        context = {
            'heading':this_article.heading,
            'body' : this_article.body,
            'reporter' : this_article.reporter.name if this_article.reporter else '',
            'created' : this_article.created,
            'image' : this_article.image.url if this_article.image else False
        }
        return render(request, 'all.html', context)
    else:
        return HttpResponseNotFound("Article not found")

def allnews(request):
    all_articles = Article.objects.all()
    if all_articles:
        context = {
            'all_articles': all_articles
        }
        return render(request, 'all.html', context)
    else:
        return HttpResponseNotFound("Article not found")
