from django.shortcuts import render
from category.models import Category
from product.models import product, productimage


# Create your views here.
def home(request):
    bull = Category.objects.all()
    context = {"ctg":bull}
    return render(request, 'index-2.html', context)

