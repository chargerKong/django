from django.shortcuts import render
from django.http import HttpResponse
from common.models import Goods,Users,Orders,Detail
from django.db.models import Q
from django.core.paginator import Paginator
 #引入随机函数模块
def index(request,pIndex=1):
    # 获取所有订单
    mod = Orders.objects.all()
    mywhere=[]
    # 搜索操作

    state = request.GET.get('select','-1')
    search = request.GET.get('search','')
    if search!='':
        mod = mod.filter(Q(linkman__contains=search)|Q(address__contains=search))
        mywhere.append('search='+search)
    if state !='-1':
        mod = mod.filter(state = state)
        mywhere.append('select='+state)
    where = "&".join(mywhere)
    # 遍历添加订单人信息
    for i in mod:
        ob = Users.objects.filter(id=i.uid).values('name')
        i.username = (ob[0]['name'])

    print(where)
    # 分页操作
    p = Paginator(mod,2)
    if int(pIndex) > p.num_pages:
        pIndex = p.num_pages
    if int(pIndex) < 1:
        pIndex = 1 
    nowPage = p.page(pIndex)
    plist = p.page_range
    # print(type(pIndex))
    context={'data':nowPage,'list3':plist,'pindex':int(pIndex),'where':where}
    return render(request,"myadmin/order/index.html",context)

def detail(request,oid):
    ''' 订单详情信息 '''
    try:
        # 加载订单信息
        orders = Orders.objects.get(id=oid)
        orders.name = Users.objects.get(id=orders.uid).name 
        
        # 加载订单详情
        dlist = Detail.objects.filter(orderid=oid)
        # 遍历每个商品详情，从Goods中获取对应的图片

        for i in dlist:
            mod = Goods.objects.get(id = i.goodsid)
            i.picname = mod.picname
        # for og in dlist:
        #     og.picname = Goods.objects.only('picname').get(id=og.goodsid).picname

        # # 放置模板变量，加载模板并输出
        context = {'orders':orders,'detaillist':dlist}
       
        
        
        return render(request,"myadmin/order/detail.html",context)
    except Exception as err:
        print(err)
        context = {'info':'没有找到要修改的信息！'}
    return render(request,"myadmin/info.html",context)


def state(httpRequest):
	pass
