# Generated by Django 5.1.6 on 2025-02-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_customer_date_customer_time_alter_customer_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date', models.DateField(default='2025-01-01')),
                ('time', models.TimeField(default='00:00')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
