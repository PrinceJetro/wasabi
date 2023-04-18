from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout #add thi
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import *


# Create your views here.

def home(request):
    if request.method=="post":
        pass
    else:
        return render(request, "index.html")


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = Jeff.objects.all()
        return render(request, 'index.html', {'form': form})


        