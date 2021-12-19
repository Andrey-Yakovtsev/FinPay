from django.db import models
from django.db.models import Count, Q


class Category(models.Model):
    name = models.CharField('Группа товара', max_length=64)


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Группа')
    name = models.CharField('Название товара', max_length=128)
    price = models.DecimalField('Стоимость единицы, руб.', max_digits=10, decimal_places=2)


'''
а) С помощью Django ORM выбрать товары, цена которых больше или равна 100 руб., 
сгруппировать по категориям и посчитать количество товаров в каждой категории.

'''
def select_goods_with_price_100plus():
    hundred_plus_goods = Count('product', filter=Q(price__gte=100))
    categories = Category.objects.annotate(hundred_plus_goods=hundred_plus_goods)
    for category in categories:
        print(f'Category {category.name} contains {category.hundred_plus_goods} goods with price 100+')



'''
б) То же самое, но оставить лишь категории, в которых строго больше 10 товаров
'''
def select_goods_with_price_100plus():
    hundred_plus_goods = Count('product', filter=Q(price__gte=100))
    categories = Category.objects.annotate(hundred_plus_goods=hundred_plus_goods)
    for category in categories:
        if category.hundred_plus_goods > 10:
            print(f'Category {category.name} contains {category.hundred_plus_goods} goods with price 100+')

'''

в) Написать код python, который выводит в консоль перечень всех товаров. Каждая строка должна содержать следующие данные:
• название категории товара,
• наименование товара, • цена.
По возможности, минимизировать количество обращений к базе данных и количество передаваемых данных
'''

def get_all_products_from_DB():
    products = Product.objects.select_related('category').all()
    for product in products:
        print(f'Категория {product.category}'
              f'Товар {product.name}',
              f'Цена {product.price}'
              )

'''
Additional questions
1. Suppose we have several independent models which have some fields in common. 
What type of django model inheritance should be used to avoid typing those common 
fields definitions in each model?

Ответ ==> i. Proxy models

2. Suppose we have model with a custom manager:
class CustomManager(models.Manager): 
    def get_queryset(self): 
    return CustomQuerySet(self.model, using=self._db)
class Item(models.Model):
    name = models.CharField('Item', max_length=100) 
    active = models.BooleanField('Active', default=True) 
    objects = CustomManager()
Now we want the following code to work: 
Item.objects.filter(pk=1).delete() - should set “active” attribute to False on matched records. 
Item.objects.filter(pk=1).delete_real() - should delete matched records from db.
What is the correct CustomQuerySet implementation?

Ответ ==> ii.
class CustomQuerySet(QuerySet):
    def delete(self): self.update(active=False)
    def delete_real(self): super(CustomQuerySet, self).delete()


3. Suppose we have model:
class Person(models.Model):
    name = models.CharField('Item', max_length=100) 
    birthday = models.DateField(...)
We want to define a model field “birthday” such that django admin interface doesn't allow 
this field to be empty, but we can create persons with empty birthday using orm 
( Person.objects.create(name='Name 1') should work).
What is the correct field definition?


Ответ ==> ii.
birthday = models.DateField(null=False, blank=True) 
'''


'''
This text for commit which will be deleted after
'''