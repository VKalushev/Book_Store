from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],default=1)
    author = models.CharField(max_length=100,default="UNKNOWN")
    is_best_selling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - Rating: {self.rating}, Written By: {self.author}"
