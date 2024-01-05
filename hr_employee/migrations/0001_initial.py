# Generated by Django 2.0 on 2024-01-03 00:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=10, unique=True, verbose_name='Employee ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(default='@gmail.com', max_length=50, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('employment_status', models.BooleanField(default=True, verbose_name='Active?')),
                ('bank_account', models.CharField(max_length=20, verbose_name='Bank Account')),
                ('bank_name', models.CharField(max_length=50, verbose_name='Bank Name')),
                ('joining_date', models.DateField(default=django.utils.timezone.now, verbose_name='Joining Date')),
                ('identity_number', models.CharField(max_length=30, verbose_name='Identity Number')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('marital_status', models.CharField(default='Single', max_length=10, verbose_name='Marital Status')),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now, verbose_name='Date of Birth')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('gender', models.CharField(default='Other', max_length=10, verbose_name='Gender')),
                ('citizen', models.CharField(default='Myanmar', max_length=50, verbose_name='Citizen')),
                ('picture', models.ImageField(blank=True, default=None, upload_to='employee/', verbose_name='Picture')),
            ],
        ),
    ]
