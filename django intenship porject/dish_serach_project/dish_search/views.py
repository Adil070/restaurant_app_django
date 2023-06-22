from django.db.models import Q
from django.shortcuts import render
from .models import Dish

from django.core.paginator import Paginator


def search(request):
    query = request.GET.get('q')
    results = Dish.objects.all()

    if query:
        results = results.filter(name__icontains=query)

    paginator = Paginator(results, 10)  # Show 10 results per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'query': query}
    return render(request, 'dish_search/search.html', context)
