from django.db import models

__all__ = (
    'FacebookUser',
)


# 이 경우는 팔로우와 달리 페이스북 친구 신청의 경우에 더 맞다.
# 일방적인 팔로우 경우는 표현하지 못한다/ 즉 방향성이 없는 대칭 관계이다
class FacebookUser(models.Model):
    # 자기자신(FacebookUser ('self'))를 참조해서
    # friends필드를 M2M으로 정의
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField(
        'self',
        blank=True,
    )

    def __str__(self):
        return self.name
