from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

def welcome(request):
    dis = Category.dis_name()
    return render(request,'home.html',{"dis":dis})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"categories": searched_categories})

    else:
        message = "Enter new search"
        return render(request, 'search.html',{"message":message})

def category(request,category_id):
    try:
        category = Category.objects.get(id = category_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"category", {"category":category})