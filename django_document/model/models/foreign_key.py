from django.db import models

__all__ = (
    'Manufacturer',
    'Car',
    'User',
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


# recursive relationship
class User(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # 한 유저가 자기 자신의 teacher로 저장될 수 없게 하기
        # teacher가 존재해야함
        if self.teacher and self.teacher.pk == self.pk:
            self.teacher = None
            return
        else:
            super(User, self).save(*args, **kwargs)