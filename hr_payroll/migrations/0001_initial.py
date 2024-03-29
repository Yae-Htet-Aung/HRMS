# Generated by Django 2.2 on 2024-01-05 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PayrollModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payroll', models.CharField(max_length=10, unique=True, verbose_name='Payroll ID')),
                ('salary', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('bonus', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('ot', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('fine', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('remark', models.TextField()),
            ],
        ),
    ]
