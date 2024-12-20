from django.http import HttpResponse
from django.shortcuts import render
from newsapi import NewsApiClient
from django.contrib.auth.decorators import login_required

def homepage(request):
    api = NewsApiClient(api_key='ffc37e25977c40738d75ea00bb025dfd')
    news_data=api.get_top_headlines(page_size=20)
    articles=news_data.get('articles',[])
    article_with_images=[article for article in articles if article.get('urlToImage')]
    context= {'articles': article_with_images}

    return render(request, 'homepage.html',context)

@login_required
def world(request):
    
    api = NewsApiClient(api_key='ffc37e25977c40738d75ea00bb025dfd')
    news_data=api.get_everything(q='world',page_size=20)
    articles=news_data.get('articles',[])
    article_with_images=[article for article in articles if article.get('urlToImage')]
    context= {'articles': article_with_images}
    
    return render(request, 'world.html',context)

@login_required
def music(request):
    api = NewsApiClient(api_key='ffc37e25977c40738d75ea00bb025dfd')
    news_data=api.get_everything(q='music OR albums OR songs OR band OR gutar OR drums OR artist',page_size=20)
    articles=news_data.get('articles',[])
    article_with_images=[article for article in articles if article.get('urlToImage')]
    context= {'articles': article_with_images}

    return render(request, 'world.html',context)

@login_required
def entertainment(request):
    api = NewsApiClient(api_key='ffc37e25977c40738d75ea00bb025dfd')
    news_data=api.get_everything(q='entertainment OR hollywood  OR bollywood OR star OR movie OR trailer OR actor OR actress',page_size=20)
    articles=news_data.get('articles',[])
    article_with_images=[article for article in articles if article.get('urlToImage')]
    context= {'articles': article_with_images}

    return render(request, 'world.html',context)

@login_required
def sports(request):
    api = NewsApiClient(api_key='ffc37e25977c40738d75ea00bb025dfd')
    news_data=api.get_everything(q='sports OR football OR cricket OR basketball OR NBA OR hockey OR olympics OR chess OR tennis OR team OR club',page_size=20)
    articles=news_data.get('articles',[])
    article_with_images=[article for article in articles if article.get('urlToImage')]
    context= {'articles': article_with_images}

    return render(request, 'world.html',context)

@login_required
def business(request):
    api = NewsApiClient(api_key='ffc37e25977c40738d75ea00bb025dfd')
    news_data=api.get_everything(q='business OR company OR takeover OR ceo OR share OR market OR stock',page_size=20)
    articles=news_data.get('articles',[])
    article_with_images=[article for article in articles if article.get('urlToImage')]
    context= {'articles': article_with_images}

    return render(request, 'world.html',context)