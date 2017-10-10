from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    # 자기자신(FacebookUser ('self'))를 참조해서
    # friends필드를 M2M으로 정의
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField(
        'self',
        blank=True,
    )