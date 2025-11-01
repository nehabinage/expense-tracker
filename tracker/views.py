from django.shortcuts import render, redirect
from .models import Expense

def home(request):
    expenses = Expense.objects.all()
    total = sum(exp.amount for exp in expenses)
    return render(request, 'home.html', {'expenses': expenses, 'total': total})

def add_expense(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        Expense.objects.create(name=name, amount=amount, category=category)
        return redirect('/')
    return render(request, 'add_expense.html')
