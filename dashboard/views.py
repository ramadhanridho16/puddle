from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Category, Item


# @login_required
# def index(request):
#     items = Item.objects.filter(created_by=request.user)

#     return render(request, 'dashboard/index.html', {
#         'items': items,
#     })

@login_required
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'dashboard/index.html', {
        'categories': categories,
        'items': items,
    })
