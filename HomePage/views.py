from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    return render (request,'home.html')


def josue(request):
    return render ( request,'josue.html')

def essai(request):
    list_produit=Product.objects.all()
    context={'list_product':list_produit}
    return render(request,'article.html', context)

def detail(request, id_article):
    article = Product.objects.get(id=id_article)
    list_produit=Product.objects.all()
    context={'list_product':list_produit}
    return render(request,'detail.html',{"article":article,'list_product':list_produit})

def search(request):
    query = request.GET['article']
    liste_article = Product.objects.filter(category__icontains =query)
    return render(request,'search.html',{'liste_article':liste_article})