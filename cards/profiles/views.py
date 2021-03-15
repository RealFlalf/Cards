from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, DetailView
from .forms import UserRegisterForm, UserLoginForm, CreateCardForm, CreateCardPostForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django import http
from .models import Card, CardPost


# Create your views here.

def view_card(request, card_id):
    card_item = Card.objects.get(pk=card_id)
    create_post_form = CreateCardPostForm
    if request.method == 'POST':
        form = CreateCardPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data['card'] = card_item
            CardPost.objects.create(**form.cleaned_data)
    return render(request, 'view_card.html', {'card_item': card_item, 'create_post_form': create_post_form})


def home_profiles(request):
    return render(request, 'home_profiles.html')


def create_card(request):
    if request.method == 'POST':
        form = CreateCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data['owner'] = request.user
            Card.objects.create(**form.cleaned_data)
            return render(request, 'home_profiles.html')
    else:
        form = CreateCardForm
    return render(request, 'create_card.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context=context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')
