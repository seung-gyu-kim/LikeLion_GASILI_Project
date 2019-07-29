from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # 추가할 필드(field)를 작성(gender, birth_date 추가)
    GENDERS = (
        ('M', '남성(Man)'),
        ('W', '여성(Woman)'),
    )
    gender = models.CharField(verbose_name='성별', max_length=1, choices=GENDERS)
    birthdate = models.DateField(verbose_name='생년월일')
    nickname = models.CharField(verbose_name='닉네임', max_length=15, unique=True)