from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from .views import latest, article_details, allnews
def headlines(request):
    return HttpResponse('<H1> Ivanka visited Hyderabad!</H1>')

urlpatterns = [
    url(r'^news/', headlines),
    url(r'^latest$', latest),
    url(r'^all$', allnews),
    url(r'^(?P<pk>\d+)$', article_details),

]
