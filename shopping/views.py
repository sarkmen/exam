from django.shortcuts import render, redirect, get_object_or_404

from .models import Category, Shop
from .forms import CategoryForm, ShopForm


def index(request):
    return render(request, 'shopping/index.html')


def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('shopping:category_detail', category.pk)
    else:
        form = CategoryForm()
    return render(request, 'shopping/category_form.html', {
        'form' : form
        })


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('shopping:category_detail', category.pk)
    else:
        form = CategoryForm()
    return render(request, 'shopping/category_form.html', {
        'form' : form
        })


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'shopping/category_detail.html', {
        'category' : category
        })


def shop_new(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.category = category
            shop.save()
            return redirect('shopping:shop_detail', category.pk, shop.pk)
    else:
        form = ShopForm()
    return render(request, 'shopping/shop_form.html', {
        'form' : form,
        })


def shop_edit(request, category_pk, pk):
    category = get_object_or_404(Category, pk=category_pk)
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.category = category
            shop.save()
            return redirect('shopping:shop_detail', category.pk, shop.pk)
    else:
        form = ShopForm()
    return render(request, 'shopping/shop_form.html', {
        'form' : form,
        })


def shop_detail(request, category_pk, pk):
    category = get_object_or_404(Category, pk=category_pk)
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'shopping/shop_detail.html', {
        'category' : category,
        'shop' : shop,
        })