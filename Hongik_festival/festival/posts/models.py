from django.conf import settings
from django.db import models


class TimeStampedModel(models.Model):
    """Base Model"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    """ Post Model """
    title = models.CharField(max_length=140)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='posts'
        )
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    text = models.TextField(max_length=200)
    how_many = models.IntegerField(default=1) # 몇대몇 미팅을 구하는지 인원수 
    
    @property
    def comment_count(self):
        return self.comments.count()

    def __str__(self):
        return f'{self.title}-{self.creator}'

    class Meta:
        ordering = ['-created_at']

        
class Comment(TimeStampedModel):
    """ Comment Model """
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='comments'
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,
        null=True,
        default='알수없음',
    )
    message = models.TextField()
    
    def __str__(self):
        return f'{self.post}-{self.creator}'

    class Meta:
        ordering = ['-created_at']    
        
        