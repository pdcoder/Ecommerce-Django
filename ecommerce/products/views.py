from django.shortcuts import render
from django.views.generic.list.ListView
# Create your views here.

from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/product_list.html",context)