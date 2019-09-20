from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # on_delete=models.CASCADE == 'Article이 삭제되면 Comment도 함께 삭제'
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #마지막에 생성된 댓글부터 역순으로 가져오게함
    class Meta:
    
        ordering = ['-pk']

    def __str__(self):
        return self.content