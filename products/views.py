from django.shortcuts import render
from django.db.models import Q

# Create your views here.

from .models import Products
from .forms import ProductsForm

def product_det_view(request):
    obj = Products.objects.get(ID = 3)
    details = {  
    'title' : obj.title,
    'price' : obj.price, 
    'tipo' : obj.tipo,
    'country': obj.country,
    'quantity' : obj.quantity,
    'Language' : obj.Language,
    'Card_condition' : obj.Card_condition,
    'Game_condition' : obj.Game_condition,
    }

    return render(request, "Products/detail.html", details)

def product_forms_view(request,*args,**kwargs):
    
    M_forms = ProductsForm() #método get, não é seguro
    if request.method == "POST": # checa se é POST, mais seguro
        M_forms = ProductsForm(request.POST)
        if M_forms.is_valid(): # checa mais uma vez por segurança
            Products.objects.create(M_forms.cleaned_data )
    context = {
        "form" : M_forms
    }
    return render(request, "Products/product_form.html", context)

def get_products_view(query = None):
    queryset = []
    queries = query.split(" ")
    for x in queries:
        prod = Products.objects.filter(
            Q(title__icontains = x)
        ).distinct()
        for y in prod:
            queryset.append(y)
    return list(set(queryset))

def SearchPage(request):
    srh = request.GET['query']
    products = Products.objects.filter(title__icontains=srh)
    params = {'products': products, 'search':srh}
    return render(request, 'search page.html', params)