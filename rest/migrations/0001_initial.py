# Generated by Django 3.1.7 on 2021-06-14 10:07

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
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.PositiveIntegerField(default=0)),
                ('final_price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая цена')),
                ('in_order', models.BooleanField(default=False)),
                ('for_anonymous_user', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя категории')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SucculentProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('height', models.CharField(max_length=255, verbose_name='Высота')),
                ('flower', models.CharField(max_length=255, verbose_name='Цветок')),
                ('frequency_of_watering', models.CharField(max_length=255, verbose_name='Переодичность полива')),
                ('flower_pot_diameter', models.CharField(max_length=255, verbose_name='Диаметр цветочного горшка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('qty', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='rest.cart', verbose_name='Корзина')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.customer', verbose_name='Покупатель')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rest.customer', verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='rest.CartProduct'),
        ),
        migrations.CreateModel(
            name='CactusProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('needles', models.CharField(max_length=255, verbose_name='Иголки')),
                ('flower', models.CharField(max_length=255, verbose_name='Цветок')),
                ('height', models.CharField(max_length=255, verbose_name='Высота')),
                ('frequency_of_watering', models.CharField(max_length=255, verbose_name='Переодичность полива')),
                ('flower_pot_diameter', models.CharField(max_length=255, verbose_name='Диаметр цветочного горшка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
