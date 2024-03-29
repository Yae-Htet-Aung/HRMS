# Generated by Django 2.0 on 2024-01-03 00:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('reason', models.TextField(blank=True, max_length=500)),
                ('claimed_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('approved_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('currency', models.CharField(default='USD', max_length=5)),
                ('payment_name', models.CharField(max_length=100)),
                ('payment_description', models.TextField(max_length=200)),
                ('payment_date', models.DateField(default=django.utils.timezone.now)),
                ('claimed_date', models.DateField(default=django.utils.timezone.now)),
                ('approval_date', models.DateField(default=django.utils.timezone.now)),
                ('receipt_image', models.ImageField(default=None, upload_to='receipt/')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('rejected', 'Rejected'), ('approved', 'Approved')], default='pending', max_length=20)),
                ('comments', models.TextField()),
                ('note', models.TextField(blank=True, max_length=300, verbose_name='Note')),
            ],
        ),
    ]
