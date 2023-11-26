from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50, db_index=True)
    slug = models.CharField(max_length=50, unique=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class ProductInvest(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    price_now = models.FloatField()
    price_change = models.CharField(max_length=50)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title
