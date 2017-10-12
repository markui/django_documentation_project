from django.db import models

__all__ = (
    'Place',
    'Restaurant',
    'Supplier',
)


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name


# place_ptr_id one-to-one과 같은 field를 django에서 자동생성한다.
class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} restaurant'


class Supplier(Place):
    #place_ptr = models.OneToOneField(Place)
    supply_places = models.ManyToManyField(
        'Place',
        related_name='supply_place_set',
        related_query_name='supply_place', # query를 할 때, onetoonefield 역참조랑 query 기본 Place.objects.filter(supplier__=)랑 똑같음
        # 충돌 방지! 이제는, Place.objects.filter(supply_place__=)
    )
