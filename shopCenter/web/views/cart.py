from django.shortcuts import render
from django.http import HttpResponse
from common.models import Users,Types,Goods
import hashlib
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

# 建立公共的函数
def loadinfo(httpRequest):
	'''获取所有的一级元素'''
	mod = Types.objects.filter(pid = 0)
	data = {"typelist":mod}
	return data

def index(httpRequest):
	data = loadinfo(httpRequest)
	# del httpRequest.session['shoplist']['total']
	# print(httpRequest.session['shoplist'])
	if 'shoplist' not in httpRequest.session:
		httpRequest.session['shoplist'] = {}
	

	# httpRequest.session['total'] = 0
	# return HttpResponse(httpRequest.session['shoplist'])
	return render(httpRequest,'web/cart.html',data)

def add(httpRequest,gid):
	# del httpRequest.session['shoplist']
	# 转换为整形
	
	# 获取商品的信息
	mod = Goods.objects.get(id = gid).toDict()
	# mod = mod.
	m = int(httpRequest.POST.get('m',0))

	mod['m'] = m
	# 获取session键为shoplist的信息，没有返回{}

	shoplist = httpRequest.session.get('shoplist',{})
	
	
	# shoplist的形式  {1：{},2:{},3:{}，}
	# 询问的是键是否在shoplist中
	if gid in shoplist:
		# 如果在的话，里面的m就增加
		shoplist[gid]['m'] += m
	else:
		# 否则就把新的字典加进去
		shoplist[gid] = mod
	# 放回session中
	httpRequest.session['shoplist'] = shoplist
	# print(httpRequest.session['shoplist'])

	return redirect(reverse('cart_index'))

def delete(httpRequest,gid):
	shoplist = httpRequest.session['shoplist']
	del shoplist[gid]
	httpRequest.session['shoplist'] = shoplist
	return redirect(reverse('cart_index'))

def clear(httpRequest):
	httpRequest.session['shoplist'] = {}
	return redirect(reverse('cart_index'))

def change(httpRequest):
	gid = httpRequest.GET.get("gid")
	shoplist = httpRequest.session['shoplist']
	num = int(httpRequest.GET.get("num"))
	if num<1:
		num = 1
	shoplist[gid]['m'] = num
	httpRequest.session['shoplist']= shoplist
	
	return redirect(reverse('cart_index'))