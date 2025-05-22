from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Transaction, Categories
from .forms import TransactionForm, UserRegistrationForm, UserLoginForm, AddCategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from .utils import q_search
from django.contrib.auth.forms import AuthenticationForm



def dashboard(request):
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(user=request.user).order_by('date')[:5]
        balance = sum(t.amount if t.type == "Income" else -t.amount for t in transactions)
        return render(request, 'main/dashboard.html', {'transactions':transactions, 'balance': balance})
    else:
        return render(request, 'main/dashboard.html')
@login_required
def filtered_transactions(request):    
    transactions = Transaction.objects.filter(user=request.user)
    balance = sum(t.amount if t.type == "Income" else -t.amount for t in transactions)
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    category = request.GET.get("category")
    min_amount = request.GET.get("min_amount")
    max_amount = request.GET.get("max_amount")
    
    
    
    filtered_qs = q_search(
        qs=transactions,
        start_date=start_date,
        end_date=end_date,
        category=category,
        min_amount=min_amount,
        max_amount=max_amount,
    )


    categories = Categories.objects.all()
    return render(
        request,
        "main/transactions_list.html",
        {"transactions": filtered_qs, "balance": balance, "categories": categories},
    )

@login_required
def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, "Транзакция успешно добавлена")
            return redirect("main:dashboard")

    else:
        form = TransactionForm()

    return render(request, "main/add_transactions.html", {"form": form})


@login_required
def get_transactions(request):
    qs = Transaction.objects.filter(user=request.user).order_by('-date')
    

    categories = Categories.objects.all()


    
    return render(
        request,
        "main/transactions_list.html",
        {"transactions": qs, "categories": categories},
    )


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        print(f"Form data: {request.POST}")
        print(f"Form is valid: {form.is_valid()}")

        if form.is_valid():  # Добавлены скобки
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            print(f"Authenticated user: {user}")
            
            if user:
                auth.login(request, user)
                print("User logged in")
                return redirect("main:dashboard")
            else:
                print("Authentication failed")
        else:
            print(f"Form errors: {form.errors}")  # Печать ошибок формы
    else:
        form = UserLoginForm()
    
    return render(request, "registration/login.html", {"form": form})


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect("main:dashboard")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/registration.html", {"form": form})


@login_required
def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('main:dashboard')
    else:
        form = AddCategoryForm()
    return render(request, 'main/add_category.html', {'form': form})        

def logout(request):
    auth.logout(request)
    return redirect('main:dashboard')
