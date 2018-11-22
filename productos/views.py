from django.http import HttpResponse
from django.shortcuts import render

from .models import Productos, Categorias

def index(request):
    productos = Productos.objects.all()
    context = {
        'title': 'Productos',
        'productos': productos
    }
    return render(request, 'productos/index.html', context)

def cats(request):
    categorias = Categorias.objects.all()
    context = {
        'title': 'Categorias',
        'categorias': categorias
    }
    return render(request, 'productos/categorias.html', context)

def edit(request, id):
    producto = Productos.objects.get(id = id)
    if (request.method == "POST"):
        producto.cost = request.POST.get('cost')
        producto.quantity = request.POST.get('quantity')
        producto.save()

    context = {
            'producto': producto
    }

    return render(request, 'productos/edit.html', context)

def catedit(request, id):
    categoria = Categorias.objects.get(id = id)
    if (request.method == "POST"):
        categoria.name = request.POST.get('name')
        categoria.desc = request.POST.get('desc')
        categoria.save()

    context = {
            'categoria': categoria
    }

    return render(request, 'productos/catedit.html', context)

def crear(request):
    context = {}
    if(request.method == "POST"):
        Productos.objects.create(name=request.POST.get('name'), cost=request.POST.get('cost'), quantity=request.POST.get('quantity'))
    return render(request, 'productos/crear.html', context)

def crearcat(request):
    context = {}
    if(request.method == "POST"):
        Categorias.objects.create(name=request.POST.get('name'), desc=request.POST.get('desc'))
    return render(request, 'productos/crearcat.html', context)

def eliminar(request, id):
    producto = Productos.objects.get(id = id)
    producto.delete()
    return render(request, 'productos/eliminar.html')

def catdelete(request, id):
    categoria = Categorias.objects.get(id = id)
    categoria.delete()
    return render(request, 'productos/catdelete.html')

def save(request, id):
    return render(request, 'productos/edit.html', context)

def comprar(request, id):
    producto = Productos.objects.get(id = id)

    context = {
            'producto': producto
    }

    if(request.method == "POST"):
        cantidad = request.POST.get('qty')
        if(int(cantidad) > int(producto.quantity) or int(cantidad) <= 0):
            return error(request)
        else:
            producto.quantity -= int(cantidad)
            producto.save()
            return render(request, 'productos/comprar.html', context)

    return render(request, 'productos/comprar.html', context)

def error(request):
    return render(request, 'productos/error.html')