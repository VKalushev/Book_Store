from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],default=1)
    author = models.CharField(max_length=100,default="UNKNOWN")
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(default="",null=False,db_index=True)

    def __str__(self):
        return f"{self.title} - Rating: {self.rating}, Written By: {self.author}"
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])
    
