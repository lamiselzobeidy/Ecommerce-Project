# Generated by Django 3.0.3 on 2020-03-19 13:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('name', models.CharField(max_length=120)),
                ('brand', models.IntegerField(primary_key=True, serialize=False)),
                ('brand_img', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_name', models.CharField(max_length=120)),
                ('cat_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cat_description', models.CharField(max_length=400)),
                ('cat_image', models.ImageField(default='default.jpg', upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='')),
                ('DOB', models.DateTimeField(blank=True, default=datetime.date.today)),
                ('location', models.CharField(default='None', max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('subcat_name', models.CharField(max_length=120)),
                ('subcat_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subcat_description', models.CharField(max_length=300)),
                ('subcat_image', models.ImageField(upload_to='gallery')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshopping.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_name', models.CharField(max_length=120)),
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_price', models.IntegerField()),
                ('slug', models.SlugField()),
                ('image1', models.ImageField(upload_to='gallery')),
                ('image2', models.ImageField(upload_to='gallery')),
                ('image3', models.ImageField(upload_to='gallery')),
                ('product_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshopping.Brand')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='subcat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshopping.SubCategory'),
        ),
    ]
