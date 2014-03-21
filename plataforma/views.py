from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def menu(request):
    return render(request,'menu.html')

@login_required
def login_page(request):
    return render(request,'login_page.html')