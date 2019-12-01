from django.conf import settings
from django.db import models
from posts.models import TimeStampedModel


class Bar(TimeStampedModel):
    """ Bar Model """
    name = models.CharField(max_length=80)
    represent_image = models.ImageField(upload_to='bars')
    first_image = models.ImageField(upload_to='bars')
    second_image = models.ImageField(upload_to='bars')
    third_image = models.ImageField(upload_to='bars')
    text = models.TextField(max_length=200) # 술집에 대한 간단한 소개
    location_url = models.TextField(max_length=200) # 술집 위치 -> 이후 필요에 따라 변경될 가능성이 높은 필드

    @property
    def barlike_count(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.name}'

# 입시 모델 - 필요에 따라 삭제될 수 있는 모델
class BarLike(TimeStampedModel):
    """ BarLike Model """
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE, related_name='likes')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.bar.name}-{self.creator.name}'
    
