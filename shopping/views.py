from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Category, Shop, Review
from .forms import CategoryForm, ShopForm, ReviewForm


def index(request):
    category_list = Category.objects.all()
    review_list = Review.objects.all().order_by('-created_at')[:9]
    return render(request, 'shopping/index.html', {
        'category_list' : category_list,
        'review_list' : review_list,
        })

@login_required
def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, '새로운 카테고리가 등록되었습니다.')
            return redirect('shopping:category_detail', category.pk)
    else:
        form = CategoryForm()
    return render(request, 'shopping/category_form.html', {
        'form' : form
        })


@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            messages.success(request, '카테고리가 수정되었습니다.')
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


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.error(request, "카테고리가 삭제되었습니다.")
    return redirect('shopping:index')



@login_required
def shop_new(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.category = category
            shop.save()
            messages.success(request, '새로운 가게가 등록되었습니다.')
            return redirect('shopping:shop_detail', category.pk, shop.pk)
    else:
        form = ShopForm()
    return render(request, 'shopping/shop_form.html', {
        'form' : form,
        })


@login_required
def shop_edit(request, category_pk, pk):
    category = get_object_or_404(Category, pk=category_pk)
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.category = category
            shop.save()
            messages.success(request, '가게가 수정되었습니다.')
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


@login_required
def shop_delete(request, category_pk, pk):
    shop = get_object_or_404(Shop, pk=pk)
    shop.delete()
    messages.error(request, "가게가 삭제되었습니다.")
    return redirect('shopping:category_detail', category_pk)


@login_required
def review_new(request, category_pk, shop_pk):
    category = get_object_or_404(Category, pk=category_pk)
    shop = get_object_or_404(Shop, pk=shop_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = shop
            review.user = request.user
            review.save()
            messages.success(request, '새로운 리뷰가 등록되었습니다.')
            return redirect('shopping:shop_detail', category.pk, shop.pk)
    else:
        form = ReviewForm()
    return render(request, 'shopping/review_form.html', {
        'form' : form,
        })


@login_required
def review_edit(request, category_pk, shop_pk, pk):
    category = get_object_or_404(Category, pk=category_pk)
    shop = get_object_or_404(Shop, pk=shop_pk)
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = shop
            review.user = request.user
            review.save()
            messages.success(request, '리뷰가 수정되었습니다.')
            return redirect('shopping:shop_detail', category.pk, shop.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'shopping/review_form.html', {
        'form' : form
        })


@login_required
def review_delete(request, category_pk, shop_pk, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    messages.error(request, "리뷰가 삭제되었습니다.")
    return redirect('shopping:shop_detail', category_pk, shop_pk)