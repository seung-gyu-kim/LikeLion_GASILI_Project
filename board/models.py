from django.db import models

# Create your models here.

class Board(models.Model) :
    #pk = models.AutoField()
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20)
    body = models.TextField()
    product_price = models.PositiveIntegerField(blank=True,default=0)
    order_price = models.PositiveIntegerField(default=0)
    state = models.CharField(max_length=15)
    userId = models.IntegerField()
    userName = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', blank=True)
    image1 = models.ImageField(upload_to='images/', blank=True)
    image2 = models.ImageField(upload_to='images/', blank=True)
    image3 = models.ImageField(upload_to='images/', blank=True)
    image4 = models.ImageField(upload_to='images/', blank=True)
    image5 = models.ImageField(upload_to='images/', blank=True)

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
    post = models.IntegerField()
    userId = models.IntegerField()
    author = models.CharField(max_length=15)
    text = models.TextField()
    price = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text