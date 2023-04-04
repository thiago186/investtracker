from django.shortcuts import render, redirect
from .forms import StockForm, InvestmentFundForm, FixedIncomeForm

# Create your views here.
def home(request):
    return render(request, 'assets/home.html', {})

def workingOn(request):
    return render(request, 'assets/workingOn.html', {})


def create_stock(request):
    form = StockForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('assets:home')
    return render(request, 'assets/create_assets.html', {'form': form})

def create_investment_funds(request):
    form = InvestmentFundForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('assets:home')
    return render(request, 'assets/create_assets.html', {'form': form})

def create_fixed_income(request):
    form = FixedIncomeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('assets:home')
    return render(request, 'assets/create_assets.html', {'form': form})