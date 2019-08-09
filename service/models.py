from django.db import models

# Create your models here.

class Service(models.Model) :
    #pk = models.AutoField()
    title = models.CharField(max_length=200)
    body = models.TextField()
    def __str__(self) :
        return self.title
    #제목
    #날짜
    #카테고리 
    #본문
    #작성자