from django.db import models

__all__ = (
    'Idol',
    'Group',
    'Membership',
)


class Idol(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    debut_date = models.DateField()
    members = models.ManyToManyField(
        'Idol',
        through='Membership',
        through_fields=('group', 'idol') # 순서는 소스 이후에 타겟 써주기
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    idol = models.ForeignKey(Idol, on_delete=models.CASCADE) # membership_set으로 참조
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    recommender = models.ForeignKey(
        Idol,
        null=True,
        on_delete=models.SET_NULL,
        related_name='recommend_membership_set', # reverse accessor 오류가 나기 때문에
    )
    # recommenders = models.ManyToManyField(
    #     'Idol',
    #     blank=True,
    #     related_name='recommend'
    # )
    joined_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.group.name}' \
               f'{self.idol.name}' \
               f'({self.is_active})'
