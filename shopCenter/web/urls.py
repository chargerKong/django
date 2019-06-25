from django.conf.urls import url
from web.views import views,cart,order,vip
from myadmin.views import index,users

urlpatterns = [
	#主页
    url(r'^$', views.index,name='index'),
    # 列表页
    url(r'^list/(?P<pindex>[0-9]+)$', views.list,name='list'),
    url(r'^list$', views.list,name='list'),
    # 详情页
    url(r'^detail/(?P<uid>[0-9]+)$', views.detail,name='detail'),

    # 会员及个人中心等路由配置
    url(r'^login$', views.login, name="login"),
    url(r'^dologin$', views.dologin, name="dologin"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^registor$', views.registor, name="registor"),
    # 执行注册，利用一下后台提交功能提交到数据库
    url(r'^doregist$', views.insert, name="doregist"),
    
    # 验证码
    url(r'^verify$', index.verify, name="myadmin_verify"),

    #  购物车路由
    url(r'^cart$', cart.index, name="cart_index"),
    url(r'^cart/add/(?P<gid>[0-9]+)$', cart.add, name="cart_add"),
    url(r'^cart/del/(?P<gid>[0-9]+)$', cart.delete, name="cart_del"),
    url(r'^cart/clear$', cart.clear, name="cart_clear"),
    url(r'^cart/change$', cart.change, name="cart_change"),

    #  订单处理
    url(r'^order$', order.index, name="order_index"),
    url(r'^order/confirm$', order.confirm, name="order_confirm"),
    url(r'^cart/insert$', order.insert, name="order_insert"),

    # 个人订单查看
    url(r'^vip/order$', vip.viporder, name="vip_viporder"),
    url(r'^vip/order/([0-9]+)$', vip.viporder, name="vip_viporder"),
    url(r'^vip/odstate$', vip.odstate, name="vip_odstate"),
    # 个人信息查询
    url(r'^vip/info$', vip.vipinfo, name="vip_vipinfo"),
    # 信息修改
    url(r'^vip/change$', vip.vipchange, name="vip_vipchange"),
    # 密码修改页面
    url(r'^vip/changPsw$', vip.changPsw, name="vip_changPsw"),
    # 密码修改
    url(r'^vip/updatePaw$', vip.updatePaw, name="vip_updatePaw"),

]
