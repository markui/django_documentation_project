from django.db import models

__all__ = (
    'InstagramUser',
)


# 방향성이 있는 경우
# symmetrical=False 주기
class InstagramUser(models.Model):
    name = models.CharField(max_length=30)
    # symmetrical=False옵션으로
    # 자기자신을 참조하는 following필드 1개 생성
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.name
