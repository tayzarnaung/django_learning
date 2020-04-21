from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Create your views here.
def index(request):
    # return HttpResponse("index")
    products = Product.objects.all()
    for pdt in products:
        print(pdt)
    return render(request, 'index.html', {'products': products})

def new(request):
    return HttpResponse("new")
