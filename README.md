# django
django 
本项目于的django版本是1.11.11

## 项目启动过程
 - 打开mysql数据库，建立shopdb数据库，把文件shopdb.sql的内容复制进去，执行
 - 进入shopcenter文件夹，右键打开命令行窗口，`python manage.py runserver`
 - 打开浏览器，输入localhost:8000 即可访问前台
 - localhost:8000/myadmin 访问后台，管理员账户密码均为admin

## 项目简介
 - 前台可分类浏览各商品信息，可注册，登录
 - 登录后可下单，查看个人信息，查看订单信息，修改订单状态等
 - 后台登录可修改密码，搜索信息（状态维持），添加商品信息，商品类别，订单信息处理等。
 
 ## 部分截图展示
 - 项目前台主界面，可登录或者注册，点击登录可以跳转到登录页面
![](https://github.com/chargerKong/django/blob/master/screenshot/%E5%95%86%E5%9F%8E%E4%B8%BB%E9%A1%B5%E9%9D%A2.jpg)

 - 登录页面
 ![](https://github.com/chargerKong/django/blob/master/screenshot/%E7%99%BB%E5%BD%95%E6%B3%A8%E5%86%8C.jpg)
 
 - 登录后的页面可以进入个人中心和我的订单
 ![](https://github.com/chargerKong/django/blob/master/screenshot/%E7%99%BB%E5%BD%95%E6%B3%A8%E5%86%8C.jpg)
 
 - 点击全部商品可以查看商品分页内容
 ![](https://github.com/chargerKong/django/blob/master/screenshot/%E5%95%86%E5%93%81%E5%88%86%E9%A1%B5%E6%B5%8F%E8%A7%88.jpg)
 
 - 购物车信息查看
 ![](https://github.com/chargerKong/django/blob/master/screenshot/%E5%95%86%E5%93%81%E6%B7%BB%E5%8A%A0%E8%B4%AD%E7%89%A9%E8%BD%A6.jpg)
 
 - 商品信息填写购买
 ![](https://github.com/chargerKong/django/blob/master/screenshot/%E5%95%86%E5%93%81%E7%BB%93%E7%AE%97.jpg)
 
 - 查看我的订单
 ![](https://github.com/chargerKong/django/blob/master/screenshot/%E8%AE%A2%E5%8D%95%E4%BF%A1%E6%81%AF%E6%9F%A5%E7%9C%8B.jpg)
 
 - 商城后台登录,账号：admin 密码: admin
 ![](https://github.com/chargerKong/django/blob/master/screenshot/%E5%95%86%E5%9F%8E%E5%90%8E%E5%8F%B0%E7%99%BB%E5%BD%95.jpg)
 
 - 登录成功后可以进行会员信息管理（包括查看信息，修改密码，添加会员），订单信息管理，商品类别管理等
 ![](https://github.com/chargerKong/django/blob/master/screenshot/%E5%90%8E%E5%8F%B0%E9%A6%96%E9%A1%B5.jpg)
 ![](https://github.com/chargerKong/django/blob/master/screenshot/%E5%90%8E%E5%8F%B0%E4%BC%9A%E5%91%98%E4%BF%A1%E6%81%AF%E6%B5%8F%E8%A7%88.jpg)
 
