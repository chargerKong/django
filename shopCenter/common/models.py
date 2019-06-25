from django.db import models
from datetime import datetime

#用户信息模型
class Users(models.Model):
    username = models.CharField(max_length=32,unique=True)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    sex = models.IntegerField(default=1)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    state = models.IntegerField(default=1)
    addtime = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'code':self.code,'sex':self.sex,'id':self.id,'username':self.username,'name':self.name,'password':self.password,'address':self.address,'phone':self.phone,'email':self.email,'state':self.state}


    class Meta:
        db_table = "users"  # 更改表名



class Types(models.Model):
    name = models.CharField(max_length=32)
    pid = models.IntegerField(default=0)
    path = models.CharField(max_length=256)

    class Meta:
        db_table = 'type'
        

class Goods(models.Model):
    typeid = models.IntegerField()
    goods = models.CharField(max_length=32)
    company = models.CharField(max_length=50)
    content = models.TextField()
    price = models.FloatField()
    picname = models.CharField(max_length=255)
    store = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    state = models.SmallIntegerField(default=1)
    addtime = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return{'id':self.id,'typeid':self.typeid,'goods':self.goods,'company':self.company,'content':self.content,'price':self.price,'picname':self.picname,'num':self.num,'clicknum':self.clicknum,'state':self.state,'store':self.store}

    class Meta:
        db_table = "goods"  # 更改表名

# 订单模型
class Orders(models.Model):
    uid = models.IntegerField()
    linkman = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    addtime = models.DateTimeField(default=datetime.now)
    total = models.FloatField()
    state = models.IntegerField()

    class Meta:
        db_table = "orders"  # 更改表名

#订单详情模型
class Detail(models.Model):
    orderid = models.IntegerField()
    goodsid = models.IntegerField()
    name = models.CharField(max_length=32)
    price = models.FloatField()
    num = models.IntegerField()

    class Meta:
        db_table = "detail"  # 更改表名