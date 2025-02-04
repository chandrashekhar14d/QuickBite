# Generated by Django 5.0.6 on 2024-06-07 11:58

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_ordercontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_username', models.CharField(max_length=100)),
                ('order_int', models.IntegerField()),
                ('quantity', models.IntegerField(default=0)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('location', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=21)),
                ('delivery_status', models.BooleanField(default=False)),
                ('subsection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.subsection')),
            ],
        ),
    ]
