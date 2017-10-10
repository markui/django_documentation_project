from django.db import models

__all__ = (
    'InstagramUser',
)


# 이 경우는 팔로우와 달리 페이스북 친구 신청의 경우에 더 맞다. 일방적인 팔로우 경우는 표현하지 못한다/ 즉 방향성이 없는 대칭 관계이다
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
