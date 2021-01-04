from django.shortcuts import render
from django.utils.http import urlquote_plus
from . import models
from .parserLogic import pexelsParser, unsplashParser

def home(request):
    return render(request, 'base.html')

def new_search(request):
    searchItem = request.POST.get('search')
    models.Search.objects.create(searchField = searchItem)
    search = str(searchItem).replace(" ", "+")
    responseList = unsplashParser.getImagesAndDownloadLinks(search)
    searchedTerm = {
        'search': search,
        "links": responseList,
    }
    return render(request, 'craigslist/new_search.html', searchedTerm)