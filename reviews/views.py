from django.shortcuts import render, get_object_or_404
from .forms import ReviewForm
from .models import Review
from django.utils import timezone
from django.shortcuts import redirect
from django import forms
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.core.cache import cache


def index(request):
        post_list = Review.objects.all().order_by("-review_date")
        paginator = Paginator(post_list, 10) # показывать по 10 записей на странице.
        page_number = request.GET.get('page') # переменная в URL с номером запрошенной страницы
        page = paginator.get_page(page_number) # получить записи с нужным смещением
        form = ReviewForm(request.POST or None, files=request.FILES or None)
        cache.clear()
        return render(request, 'index.html', {'page': page, 'paginator': paginator,'form': form}) # 

@login_required
def add_review(request):
    title = 'Добавить отзыв'
    button = 'Отправить. ТЫК!'
    if request.method == 'POST':
        form = ReviewForm(request.POST, files=request.FILES or None)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('reviews:index')
    form = ReviewForm(files=request.FILES or None)
    return render(request, 'new_post.html', {'form': form, 'title' : title, 'button' : button})

@login_required
def edit_review(request, username, post_id):
    title = 'Редактировать отзыв'
    button = 'Сохранить'
    post = get_object_or_404(Review, pk=post_id)
    if request.user != post.author:
        return redirect('reviews:index') 
    if request.method == "POST":
        form = ReviewForm(request.POST, files=request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('reviews:index')
    form = ReviewForm(request.POST or None, files=request.FILES or None, instance=post)
    return render(request, 'post_edit.html', {'form': form, 'title' : title, 'button' : button, 'post': post})