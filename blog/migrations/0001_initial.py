# Generated by Django 3.2 on 2024-04-06 13:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=100)),
                ('detail', models.TextField(default=None)),
                ('size', models.CharField(default=None, max_length=100)),
                ('quantity', models.IntegerField(default=None)),
                ('prices', models.IntegerField(default=None)),
                ('image', models.ImageField(default=None, upload_to='')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.categorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('comment', models.TextField(default=None)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.productsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_price', models.IntegerField(default=None)),
                ('total_qty', models.IntegerField(default=None)),
                ('name', models.CharField(default=None, max_length=30)),
                ('phone', models.IntegerField(default=None)),
                ('address', models.TextField(default=None)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('success', 'Success'), ('cancel', 'Cancel')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(default=None)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.productsmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=None)),
                ('created_at', models.DateTimeField(default=None)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.productsmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasketModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total', models.IntegerField(default=None)),
                ('buydate', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(default=None, upload_to='')),
                ('quantity', models.IntegerField(default=None)),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.productsmodel')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
