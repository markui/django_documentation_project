from django.db import models

__all__ = (
    'School',
    'CommonInfo',
    'Student',
    'Teacher',
)


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CommonInfo(models.Model):
    school = models.ForeignKey(
        'School',
        blank=True,
        null=True,
        related_name='%(app_label)s_%(class)s_set',  # application명, class명 => 절대 겹칠 수 없음.
        # 특히나 여러개의 inherited 된 모델을 생성할 경우에 일일이 related_name을 지정하기 번거로울 때 유용하다.
    )
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)


class Teacher(CommonInfo):
    subject = models.CharField(max_length=30)
