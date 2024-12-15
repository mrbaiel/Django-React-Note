from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    CATEGORY = (('Мужское', 'МУЖСКОЕ'),
                ('Женское', 'ЖЕНСКОЕ'),
                )
    name = models.CharField(verbose_name='Название', max_length=100)
    slug = models.SlugField(verbose_name='Слаг',blank=True, null=True)
    image = models.ImageField(verbose_name='Изображение',upload_to='img')
    desc = models.TextField(verbose_name='Описание',blank=True, null=True)
    price = models.DecimalField(verbose_name='Цена',max_digits=10, decimal_places=2)
    category = models.CharField(verbose_name='Категория',max_length=15, choices=CATEGORY, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            if Product.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{counter}'
                counter += 1
            self.slug = unique_slug
            
        super().save(*args, **kwargs)