from django.db import models


class Users(models.Model):
    full_name = models.CharField(verbose_name="Full Name", max_length=100, null=True, blank=False)
    username = models.CharField(verbose_name="Username", max_length=30, unique=True, null=True)
    telegram_id = models.PositiveBigIntegerField(verbose_name="Telegram Id", unique=True)

    def __str__(self):
        return self.username


class Product(models.Model):
    product_name = models.CharField(verbose_name="Product Name", max_length=50)
    photo = models.CharField(verbose_name="Rasm file_id", max_length=200, null=True)
    price = models.DecimalField(verbose_name="Narxi", decimal_places=2, max_digits=200)
    description = models.TextField(verbose_name="Mahsulot haqida", max_length=300)
    category_code = models.CharField(verbose_name="Kategoriya kodi", max_length=200)
    category_name = models.CharField(verbose_name="Category Nomi", max_length=200)
    subcategory_code = models.CharField(verbose_name="Ost-kategoriya kodi", max_length=34)
    subcategory_name = models.CharField(verbose_name="Ost-kategoriya nomi", max_length=30)

    def __str__(self):
        return self.product_name
