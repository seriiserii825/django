from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'GET':
        print(request.GET)
    return HttpResponse("Hello, world. You're at")

def categories(request, cat_id):
    return HttpResponse(f"Hello, world. You're at the category page {cat_id}")

def categories_by_slug(request, cat_slug):
    return HttpResponse(f"Hello, world. You're at the category page by slug {cat_slug}")

def archive(request, year):
    return HttpResponse(f"Hello, world. You're at the archive page {year}")

