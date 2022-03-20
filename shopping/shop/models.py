from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class register_user(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nickname = models.CharField(blank=True,max_length=20)
    phone = models.CharField(blank=True,max_length=11)
    # birth = models.DateField(blank=True)
    Verification_problem = models.CharField(blank=False,max_length=100)#验证问题
    Verification_answer = models.CharField(blank=False,max_length=50)#验证答案
    class Meta:
        verbose_name_plural = 'register_user'


class goods(models.Model):
    name=models.CharField(max_length=50,unique=True)#商品名称
    # price=models.FloatField()
    # slug = models.SlugField(max_length=100,db_index=True, unique=True)
    # info=models.TextField(blank=True)#商品信息
    # picture=models.ImageField(upload_to='categorys',blank=True)#商品图片
    class Meta:
        # verbose_name = "MODELNAME"
        ordering = ('name',)
        verbose_name_plural = '商品类别表'
        db_table = "商品类别"
    def __str__(self):
        return self.name
        # def get_abosolute_url(self):
            # return reverse('shop:product_list_by_category')

class product(models.Model):
    name=models.CharField(max_length=100,unique=True)#产品名称
    # slug = models.SlugField(max_length=100,db_index=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)#产品价格
    info=models.TextField(blank=True)#产品描述
    picture=models.ImageField(upload_to='categorys',blank=True)#产品图片
    category=models.ForeignKey(goods,on_delete=models.CASCADE)#所属类别
    num=models.IntegerField(default=0)#库存
    onsale=models.BooleanField(default=True)#上架
    onlinedate=models.DateTimeField(auto_now_add=True)#上线时间
    # xiugai=models.DateTimeField(auto_now_add=True)#修改日期
    class Meta:
        # verbose_name = "MODELNAME"
        verbose_name_plural = '产品类别'
        db_table = "产品类别"
        ordering = ('name',)
    # index_together = (('id','slug'),)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('shop:product_detail',args=[self.id])