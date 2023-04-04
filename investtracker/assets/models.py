from django.db import models

# Create your models here.
class Asset(models.Model):
    asset_type_choices = (
        ('stock','Ação/FII'), 
        ('investment_fund', 'fundo de investimento'),
        ('fixed income', 'renda fixa')
    )
    asset_type = models.CharField(max_length=50, choices=asset_type_choices)
    usertag1 = models.CharField(max_length=50, blank=True)
    usertag2 = models.CharField(max_length=50, blank=True)
    usertag3 = models.CharField(max_length=50, blank=True)
    native_currency = models.CharField(max_length=5)
    native_market = models.CharField(max_length=5)
    business_market = models.CharField(max_length=50, blank=True)

    class Meta:
        abstract = True

class Stock(Asset):
    ticker = models.CharField(max_length=15)
    company_name = models.CharField(max_length=100)
    external_ticker = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.ticker

class InvestmentFund(Asset):
    fund_name = models.CharField(max_length=250)
    days_to_application_cutoff = models.CharField(max_length=50)
    days_to_redemption_cutoff = models.CharField(max_length=50)
    days_to_application_liquidation = models.CharField(max_length=50)
    days_to_redemption_liquidation = models.CharField(max_length=50)
    fund_type = models.CharField(max_length=50)

    def __str__(self):
        return self.fund_name

class FixedIncome(Asset):
    name = models.CharField(max_length=250)
    type_choices = (
        ('dbn', 'debênture'),
        ('bond', 'bond'),
        ('lci', 'LCI'),
        ('lca', 'LCA'),
        ('cdb', 'CDB'),
        ('cri', 'CRI'),
        ('cra', 'CRA'),
    )
    fixed_income_type = models.CharField(max_length=50, choices=type_choices)
    due_date = models.DateField()
    index = models.CharField(max_length=15)
    coupon_period_in_months = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=5, decimal_places=3)
    
    def __str__(self):
        return self.name