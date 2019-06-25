from django.shortcuts import render
from django.http import HttpResponse
from common.models import Users,Types,Goods,Orders,Detail
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from datetime import datetime
def loadinfo(httpRequest):
	'''获取所有的一级元素'''
	mod = Types.objects.filter(pid = 0)
	data = {"typelist":mod}
	return data


def index(HttpRequest):
	id = (HttpRequest.GET.get("id",-1))
	id =id.split(",")
	print(len(id))
	data = loadinfo(HttpRequest)
	if (id)==[""]:
		data['info'] = "请选择商品"
		return render(HttpRequest,'web/ordersinfo.html',data)
	mod = HttpRequest.session.get("shoplist")
	total = 0;
	orderlist={}

	for i in mod:
		if i in id:
			total += int(mod[i]['m'])*float(mod[i]['price'])
			orderlist[i] = HttpRequest.session['shoplist'][i]
	HttpRequest.session['total'] = total
	HttpRequest.session['shoplist'] = mod
	HttpRequest.session['orderlist'] = orderlist
	data = loadinfo(HttpRequest);

	return render(HttpRequest,'web/ordersadd.html',data)

def confirm(Request):
	data = loadinfo(Request);
	if (Request.POST.get('phone','') == '') or (Request.POST.get('address','') == '') or (Request.POST.get('linkman','') == ''):
		data = {"info":"收货人姓名、电话或者住址不能为空"}
		return render(Request,'web/ordersinfo.html',data)
	return render(Request,'web/ordersconfirm.html',data)

def insert(httpRequest):
	data = loadinfo(httpRequest)
	try:
		# 添加订单
		mod = Orders();
		mod.uid = httpRequest.session['vipuser']['id']
		mod.linkman = httpRequest.POST.get('linkman')
		mod.address = httpRequest.POST.get('address')
		mod.phone = httpRequest.POST.get('phone')
		mod.code = httpRequest.POST.get('code')
		mod.addtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		mod.total = httpRequest.session['total']
		mod.state = 0
		mod.save()

		# 添加订单详情
		orderlist = httpRequest.session['orderlist']
		shoplist = httpRequest.session['shoplist']
		print(shoplist)
		for i in orderlist.values():
			print(i)
			del shoplist[str(i['id'])]
			ob = Detail()
			ob.orderid = mod.id
			ob.goodsid = i['id']
			ob.name = i['goods']
			ob.price = i['price']
			ob.num = i['m']
			ob.save()
		del httpRequest.session['orderlist']
		del httpRequest.session['total']
		httpRequest.session['shoplist'] = shoplist
		data["info"] = "订单添加成功！订单号："+str(mod.id)
		return render(httpRequest,"web/ordersinfo.html",data)
	except Exception as e:
		raise(e)
		data = {"info":"添加错误"}
		return render(httpRequest,'web/ordersinfo.html',data)
	
