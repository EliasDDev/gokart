# Generated by Django 5.1.6 on 2025-02-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_email_customer_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date',
            field=models.DateField(default='2025-02-20'),
        ),
        migrations.AddField(
            model_name='customer',
            name='time',
            field=models.TimeField(default='10:00'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
