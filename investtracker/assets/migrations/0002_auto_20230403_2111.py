# Generated by Django 3.2.18 on 2023-04-04 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixedincome',
            name='fixed_income_type',
            field=models.CharField(choices=[('dbn', 'debênture'), ('bond', 'bond'), ('lci', 'LCI'), ('lca', 'LCA'), ('cdb', 'CDB'), ('cri', 'CRI'), ('cra', 'CRA')], default='dbn', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fixedincome',
            name='name',
            field=models.CharField(default='lci', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investmentfund',
            name='fund_name',
            field=models.CharField(default=('lci', 'LCI'), max_length=250),
            preserve_default=False,
        ),
    ]