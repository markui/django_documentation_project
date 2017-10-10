from django.db import models


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


class Fruit(models.Model):
    name = models.CharField(
        max_length=100,
        primary_key=True
    )


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.manufacturer.name}-{self.name}'


class User(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )