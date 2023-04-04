from django import forms
from .models import Stock, InvestmentFund, FixedIncome

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'

class InvestmentFundForm(forms.ModelForm):
    class Meta:
        model = InvestmentFund
        fields = '__all__'

class FixedIncomeForm(forms.ModelForm):
    class Meta:
        model = FixedIncome
        fields = '__all__'