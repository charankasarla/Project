# Generated by Django 4.2.4 on 2023-08-14 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_IIN', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('quantity_sold', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('profit_earned', models.IntegerField()),
                ('revenue', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('orderdttm', models.DateTimeField()),
                ('is_received', models.BooleanField()),
                ('is_cancel', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('transactiondttm', models.DateTimeField()),
            ],
        ),
    ]
