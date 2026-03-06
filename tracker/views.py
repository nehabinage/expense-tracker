from django.shortcuts import render, redirect
from .models import Expense
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

@login_required
def home(request):
    expenses = Expense.objects.filter(user=request.user)
    total = sum(exp.amount for exp in expenses)
    return render(request, 'home.html', {'expenses': expenses, 'total': total})

def add_expense(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        Expense.objects.create(
            user=request.user,
            name=name, 
            amount=amount, 
            category=category)
        return redirect('/')
    return render(request, 'add_expense.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        # Optional: check if user exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)  # auto-login after signup
        return redirect('/')  # redirect to home page after signup

    return render(request, 'signup.html')