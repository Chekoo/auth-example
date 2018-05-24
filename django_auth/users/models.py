from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.

class User(AbstractUser):
    # blank = True 目的是让用户在注册时无需填写昵称
    nickname = models.CharField(max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass

# 两张表通过一对一的关系关联,要查询某个用户的 Profile 时，需要执行额外的跨表查询操作
class Profile(models.Model):
    nickname = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User)