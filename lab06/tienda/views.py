from itertools import product
from django.shortcuts import get_object_or_404, render

from .models import Categoria,Producto

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categoria_list = Categoria.objects.order_by('nombre')
    context={
        'product_list': product_list,
        'categoria_list':categoria_list
    }
    return render(request,'index.html', context)
    
def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request,'producto.html', {'producto': producto})

def categoria(request, categoria_id):
    product_list = Producto.objects.filter(categoria=categoria_id)[:6]
    categoria_list = Categoria.objects.order_by('nombre')
    categoria_nombre = Categoria.nombre
    context = {
        'product_list':product_list,
        'categoria_list':categoria_list,
        'categoria_nombre': categoria_nombre
    }
    return render(request,'categoria.html', context)