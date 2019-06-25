from django.shortcuts import render
from django.http import HttpResponse
from common.models import Users,Types,Goods,Orders,Detail
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from datetime import datetime
import hashlib
from django.core.paginator import Paginator
def loadinfo(httpRequest):
	'''获取所有的一级元素'''
	mod = Types.objects.filter(pid = 0)
	data = {"typelist":mod}
	return data

def viporder(httpRequest,pindex=1):
	'''浏览订单信息'''
	
	data = loadinfo(httpRequest)
	# 获取当前登录者的订单信息
	odlist = Orders.objects.filter(uid=httpRequest.session['vipuser']['id'])
	where = [];
	# 订单筛选
	state = httpRequest.GET.get('state',None)
	if state!=None:
		odlist=odlist.filter(state = state)
		where.append('state='+state)
	where = "&".join(where)
	# 分页
	p = Paginator(odlist,2) #两条数据为一页
	if int(pindex)>p.num_pages:
		p = p>num_pages
	if int(pindex)<0:
		p = 0

	odlist = p.page(pindex)
	plist = p.page_range
	print(where)
	data['where']=where
	data['plist']=plist
	data['pindex']=int(pindex)
	# 遍历订单信息查询对应的详情信息
	for od in odlist:
		delist = Detail.objects.filter(orderid = od.id)
		# 遍历订单详情，并且获取对应的商品信息
		for i in delist:
			i.picname = Goods.objects.only('picname').get(id=i.goodsid).picname
		od.detaillist = delist
	data['orderslist'] = odlist		

	return render(httpRequest,'web/viporders.html',data)
def odstate(httpRequest):
	try:
		pindex =httpRequest.GET.get('pindex')
		orderid = httpRequest.GET.get('oid')
		print(orderid)
		mod = Orders.objects.get(id=orderid);
		mod.state = httpRequest.GET.get('state')
		
		mod.save()
		return redirect(reverse('vip_viporder',args=[pindex]))
	except Exception as e:
		print (e)
		data = {"info":'订单处理失败，请联系管理员'}
		return render(httpRequest,'web/ordersinfo.html',data)

def vipinfo(httpRequest):
	data = loadinfo(httpRequest)
	return render(httpRequest,'web/vipinfo.html',data)

def vipchange(httpRequest):
	'''浏览和查看个人信息'''
	try:
		mod = Users.objects.get(id = httpRequest.session['vipuser']['id'])
		mod.name = httpRequest.POST.get('name',httpRequest.session['vipuser']['name'])
		mod.sex = int(httpRequest.POST.get('sex',httpRequest.session['vipuser']['sex']))
		mod.address = httpRequest.POST.get('address',httpRequest.session['vipuser']['address'])
		mod.code = (httpRequest.POST.get('code',httpRequest.session['vipuser']['code']))
		mod.phone = (httpRequest.POST.get('phone',httpRequest.session['vipuser']['phone']))
		mod.email = (httpRequest.POST.get('email',httpRequest.session['vipuser']['email']))
		httpRequest.session['vipuser'] = mod.toDict()
		mod.save()

		data = {'info':'修改成功'}
	except Exception as e:
		print(e)
		data = {'info':'修改失败，请联系管理员'} 
	
	return render(httpRequest,'web/vipinformation.html',data)

def changPsw(httpRequest):
	'''返回个人密码'''
	data = loadinfo(httpRequest)
	return render(httpRequest,'web/vipchangePsw.html',data)

def updatePaw(httpRequest):
	'''修改密码'''

	try:
		mod = Users.objects.get(id = httpRequest.session['vipuser']['id'])
		oldPaw = httpRequest.POST.get('old_password','')
		newPaw = httpRequest.POST.get('new_password','')
		if oldPaw == '' or newPaw == '':
			data = {'info':'请把密码填写完整'}  
			return render(httpRequest,'web/vipinformation.html',data)	
		m = hashlib.md5()
		m.update(bytes(oldPaw,encoding="utf8"))
		if mod.password == m.hexdigest():
			m = hashlib.md5()
			m.update(bytes(newPaw,encoding='utf8'))
			mod.password = m.hexdigest()
			mod.save()
			data = {'info':'密码修改成功'} 
		else:
			data = {'info':'原密码输入错误'} 
	except Exception as e:
		raise(e)
		data = {'info':'修改错误，请联系管理员'}  

	return render(httpRequest,'web/vipinformation.html',data)	