from django.db import models

class ClassBlog(models.Model):
    title = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    
    def __str__(self):
        return self.title

        