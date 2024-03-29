# Generated by Django 2.0 on 2024-01-03 00:05

from django.db import migrations, models
import hr_job.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Job Title')),
                ('description', models.TextField()),
                ('responsibilities', models.TextField()),
                ('requirements', models.TextField()),
                ('employment_type', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Contract', 'Contract'), ('Temporary', 'Temporary'), ('Internship', 'Internship')], default='Full-Time', max_length=20)),
                ('location', models.CharField(default='Yangon', max_length=200)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('published_date', models.DateTimeField(default=hr_job.models.today)),
                ('application_deadline', models.DateField(default=hr_job.models.next2months)),
                ('is_active', models.BooleanField(default=True)),
                ('company_name', models.CharField(default='yaehrms', max_length=100)),
                ('company_description', models.TextField(blank=True, null=True)),
                ('company_website', models.URLField(blank=True, default='yaehrms.com', null=True)),
                ('contact_name', models.CharField(blank=True, default='HR Department', max_length=100, null=True)),
                ('contact_email', models.EmailField(default='yaehrms@gmail.com', max_length=254)),
                ('contact_phone', models.CharField(default='09111222333', max_length=20)),
                ('benefits', models.TextField(blank=True, default='Meal allowance, Ferry, Bonus', null=True)),
                ('additional_information', models.TextField(blank=True, default='Additional Information', null=True)),
            ],
        ),
    ]
