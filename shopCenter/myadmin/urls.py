from django.conf.urls import url
from myadmin.views import index,users,types,goods,orders


urlpatterns = [
    url(r'^$', index.index,name='admin_index'),
     # 后台登录界面路由
    url(r'^login$', index.login, name="myadmin_login"),
    url(r'^dologin$', index.dologin, name="myadmin_dologin"),
    url(r'^logout$', index.logout, name="myadmin_logout"),
    url(r'^verify$', index.verify, name="verify"),

    # 后台用户管理
    url(r'^users/([0-9]+)$',users.index,name='admin_users_index'),
    url(r'^users/add$',users.add,name='admin_users_add'),
    url(r'^users/insert$', users.insert, name="myadmin_users_insert"),
    url(r'^users/del/(?P<uid>[0-9]+)$', users.delete, name="myadmin_users_del"),
    url(r'^users/edit/(?P<uid>[0-9]+)$', users.edit, name="myadmin_users_edit"),
    url(r'^users/update/(?P<uid>[0-9]+)$', users.update, name="myadmin_users_update"),
    url(r'^users/chanPaw/(?P<uid>[0-9]+)$', users.chanPaw, name="myadmin_users_chanPaw"),
    url(r'^users/editPaw/(?P<uid>[0-9]+)$', users.editPaw, name="myadmin_users_editPaw"),
    url(r'^users/search$', users.search, name="myadmin_users_search"),
    
    # 商品管理
    url(r'^types$',types.index,name='admin_types_index'),
    url(r'^types/add/(?P<pid>[0-9]+)$',types.add,name='admin_types_add'),
    url(r'^types/insert$', types.insert, name="myadmin_types_insert"),
    url(r'^types/del/(?P<uid>[0-9]+)$', types.delete, name="myadmin_types_del"),
    url(r'^types/edit/(?P<uid>[0-9]+)$', types.edit, name="myadmin_types_edit"),
    url(r'^types/update/(?P<uid>[0-9]+)$', types.update, name="myadmin_types_update"),

    # 商品信息管理
    url(r'^goods/([0-9]+)$',goods.index,name='admin_goods_index'),
    url(r'^goods/add $',goods.add,name='admin_goods_add'),
    url(r'^goods/insert$', goods.insert, name="myadmin_goods_insert"),
    url(r'^goods/del/(?P<uid>[0-9]+)$', goods.delete, name="myadmin_goods_del"),
    url(r'^goods/edit/(?P<uid>[0-9]+)$', goods.edit, name="myadmin_goods_edit"),
    url(r'^goods/update/(?P<uid>[0-9]+)$', goods.update, name="myadmin_goods_update"),
    url(r'^goods/search$', goods.search, name="myadmin_goods_search"),

     # 订单信息管理路由
    url(r'^orders$', orders.index, name="myadmin_orders_index"),
    url(r'^orders/(?P<pIndex>[0-9]+)$', orders.index, name="myadmin_orders_index"),
    url(r'^orders/detail/(?P<oid>[0-9]+)$', orders.detail, name="myadmin_orders_detail"),
    url(r'^orders/state$',orders.state, name="myadmin_orders_state"),
] 