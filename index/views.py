from django.shortcuts import render
from .models import Tourism


def index(request):
    return render(request,'index.html')

