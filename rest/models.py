from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.urls import reverse

User = get_user_model()


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Product(models.Model):
    MIN_RESOLUTION = (400, 400)
    MAX_RESOLUTION = (700, 700)
    MAX_IMAGE_SIZE = 3145728

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Фотография')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')


class CactusProduct(Product):
    needles = models.CharField(max_length=255, verbose_name='Иголки')
    flower = models.CharField(max_length=255, verbose_name='Цветок')
    height = models.CharField(max_length=255, verbose_name='Высота')
    frequency_of_watering = models.CharField(max_length=255, verbose_name='Переодичность полива')
    flower_pot_diameter = models.CharField(max_length=255, verbose_name='Диаметр цветочного горшка')

    def __str__(self):
        return "{}: {}".format(self.category.name, self.title)


class SucculentProduct(Product):
    height = models.CharField(max_length=255, verbose_name='Высота')
    flower = models.CharField(max_length=255, verbose_name='Цветок')
    frequency_of_watering = models.CharField(max_length=255, verbose_name='Переодичность полива')
    flower_pot_diameter = models.CharField(max_length=255, verbose_name='Диаметр цветочного горшка')

    def __str__(self):
        return "{}: {}".format(self.category.name, self.title)


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    object_id = models.PositiveIntegerField()
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')


class Cart(models.Model):
    owner = models.ForeignKey('Customer', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
