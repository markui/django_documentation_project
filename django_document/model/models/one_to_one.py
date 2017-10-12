from django.db import models

__all__ = (
    'Place',
    'Restaurant'
)


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.name} the place'


class Restaurant(models.Model):
    place = models.OneToOneField(
        'Place',
        on_delete=models.CASCADE,
        primary_key=True,  # 굳이 이 restaurant만의 id 가질 필요 없으므로
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.place.name} the restaurant'


class Waiter(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} the waiter at {self.restaurant}'
