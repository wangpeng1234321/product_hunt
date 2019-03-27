from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    title = models.CharField(default='例如:熊猫是兽中珍品 此烟是烟中珍品', max_length=50)
    intro = models.TextField(default='这里写APP介绍')
    url   = models.CharField(default='Http://', max_length=100)
    icon  = models.ImageField(default='default_icon.png', upload_to='images/')
    image = models.ImageField(default='default_image.jpeg', upload_to='images/')

    votes = models.IntegerField(default=1)
    pub_date = models.DateTimeField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE) #注销用户功能，用户不存在了，作品也消失了

    def __str__(self):
        return self.title
