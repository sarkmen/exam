from django.shortcuts import render, redirect, get_object_or_404

from .models import Category
from .forms import CategoryForm


def index(request):
    return render(request, 'shopping/index.html')


def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
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
        form = CategoryForm(request.POST, request.FILES, instance=category)
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



