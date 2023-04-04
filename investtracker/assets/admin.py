from django.contrib import admin
from .models import Stock, InvestmentFund, FixedIncome

# Register your models here.
admin.site.register(Stock)
admin.site.register(InvestmentFund)
admin.site.register(FixedIncome)