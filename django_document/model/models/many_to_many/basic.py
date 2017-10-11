from django.db import models

__all__ = (
    'Pizza',
    'Topping',
)


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField(
        'Topping',
        blank=True,  # 그냥 admin에서 blank 로 save한 경우 나는 에러 방지용
        # null=True는 필요없다. 애초에 이 부분은 DB에 save되는 부분이 아니기 떄문에
    )

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
