from django.db import models

__all__ = (
    'Person',
)


# Create your models here.
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=30)
    shirt_size = models.CharField(
        max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return self.name
