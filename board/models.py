from django.db import models

# Create your models here.

class Board(models.Model) :
    #pk = models.AutoField()
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    category = models.CharField(max_length=20)
    body = models.TextField()
    product_price = models.PositiveIntegerField(blank=True,default=0)
    order_price = models.PositiveIntegerField(default=0)
    state = models.CharField(max_length=20)
    userName = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self) :
        return self.title
    #제목
    #날짜
    #카테고리 
    #본문
    #상품가격
    #구입가격
    #게시물 상태
    #작성자

class Comment(models.Model):
    post = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField('date published')
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text