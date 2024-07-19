from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} - {self.code}"
    
    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city} - {self.street}, {self.postal_code}"

    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)
    published_countries = models.ManyToManyField(Country, related_name="books")

    def __str__(self):
        return f"{self.title} - Rating: {self.rating}, Written By: {self.author}"

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])
