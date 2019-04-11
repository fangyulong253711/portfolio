from django.db import models

# Create your models here.

#APP的功能
class Gallery(models.Model):
    #作品简介
    description = models.CharField(default='在这里写作品的简介',max_length=100)
    #作品图片
    image=models.ImageField(default='default.png',upload_to='images/')
    #管理员界面中作品的标题
    title = models.CharField(default='作品标题',max_length=50)


    def __str__(self):
        return self.title


