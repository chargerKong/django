from django.shortcuts import render
from django.http import HttpResponse
from common.models import Users
from django.db.models import Q
from django.core.paginator import Paginator
import hashlib
# Create your views here.
def index(httpRequest,pindex):
	'''浏览信息'''
	mod = Users.objects.all()
	keyword = httpRequest.GET.get('search',None)
	sexValue = httpRequest.GET.get('select','')
	
	where=[]
	if keyword:
		mod = mod.filter(Q(username__contains =keyword) | Q(name__contains=keyword))
		where.append('search='+keyword)
	else:
		mod = mod.filter()
	if sexValue != '' and sexValue !='-1':
		mod = mod.filter(sex = (sexValue))
		where.append('select='+sexValue)
	else:
		mod = mod.filter()
	
	where = "&".join(where)
	p = Paginator(mod,2)#两条一页
	
	list2 = p.page(pindex) #拿取第pindex页的数据
	list3 = p.page_range
	if p.num_pages == 1:
		nextPage = 1
		prePage = 1
	elif pindex == str(p.num_pages):
		nextPage = p.num_pages
		prePage = list2.previous_page_number()
		# nextPage = p.next_page_number()
	elif pindex == '1':
		prePage = '1'
		nextPage = list2.next_page_number()
	else:
		nextPage = list2.next_page_number()
		prePage = list2.previous_page_number()

	data={"data":list2,'list3':list3,'pindex':int(pindex),'nextPage':nextPage,'prePage':prePage,'where':where}
	return render(httpRequest,'myadmin/users/users.html', data)

def add(httpRequest):
	'''加载添加页面'''
	
	return render(httpRequest,'myadmin/users/add.html')

def insert(httpRequest):
	'''执行添加'''
	try:
		mod = Users()
		mod.username = httpRequest.POST.get('username',None)
		mod.name = httpRequest.POST.get('name',None)
		# mod.password = httpRequest.POST.get('password',None)
		
		#获取密码并md5
		
		m = hashlib.md5() 
		m.update(bytes(httpRequest.POST['password'],encoding="utf8"))
		mod.password = m.hexdigest()

		mod.sex = httpRequest.POST.get('sex',None)
		mod.address = httpRequest.POST.get('address',None)
		mod.phone = httpRequest.POST.get('phone',None)
		mod.email = httpRequest.POST.get('email',None)
		mod.state = 1
		mod.code = httpRequest.POST.get('code',None)
		mod.save()
		data = {"info":'添加成功'}

	except Exception as e:
		print(e)
		data = {"info":'账号已被注册添加！'}
		return render(httpRequest,'myadmin/info.html',data)

	return render(httpRequest,'myadmin/info.html',data)

def delete(httpRequest,uid):
	'''删除信息'''
	try:
		if httpRequest.session['adminuser']['id'] == int(uid):
			data = {"info":"请用别的管理员账户删除自己"}
			return render(httpRequest,'myadmin/info.html',data)
		mod = Users.objects.get(id = uid)
		
		mod.delete()
		data = {"info":'删除成功'}

	except Exception as e:
		print(e)
		data = {"info":'删除失败'}
	return render(httpRequest,'myadmin/info.html',data)


def edit(httpRequest,uid):
	'''加载编辑信息页面'''
	try:
		mod = Users.objects.get(id = uid)
		data = {"data":mod}
		return render(httpRequest,'myadmin/users/edit.html',data)
	except Exception as e:
		print(e)
		data = {"info":'加载失败，请联系管理员'}
		return render(httpRequest,'myadmin/info.html',data)
	

def update(httpRequest,uid):
	'''执行编辑更新信息'''
	try:
		mod = Users.objects.get(id=uid)
		
		mod.name = httpRequest.POST.get('name',None)
		mod.sex = httpRequest.POST.get('sex',None)
		mod.address = httpRequest.POST.get('address',None)
		mod.phone = httpRequest.POST.get('phone',None)
		mod.email = httpRequest.POST.get('email',None)
		mod.state = httpRequest.POST.get('state',None)
		mod.code = httpRequest.POST.get('code',None)
		mod.save()
		data = {"info":'修改成功'}

	except Exception as e:
		print(e)
		data = {"info":'修改失败'}
	return render(httpRequest,'myadmin/info.html',data)

def editPaw(httpRequest,uid):
	try:
		mod = Users.objects.get(id=uid)
		data = {"id":uid,"name":mod.name,"username":mod.username}
		date = {"data":data}
		return render(httpRequest,'myadmin/users/editPaw.html',date)
	except Exception as e:
		raise(e)
		data = {"info":'信息获取错误'}
		return render(httpRequest,'myadmin/info.html',data)
	

def chanPaw(httpRequest,uid):
	try:
		mod = Users.objects.get(id=uid)
		m = hashlib.md5() 
		m.update(bytes(httpRequest.POST['password'],encoding="utf8"))
		mod.password = m.hexdigest()
		mod.save()
		data = {"info":'修改成功'}
	except Exception as e:
		print(e)
		data = {"info":'修改失败'}
	return render(httpRequest,'myadmin/info.html',data)

def search(httpRequest):
	info = httpRequest.POST.get('search',None)
	sexValue = httpRequest.POST.get('select',None)
	# 判断用户到底输入什么
	if sexValue!= '-1' and info!="":
		mod = Users.objects.filter(sex = int(sexValue),username = info)
		mod1 = Users.objects.filter(sex = int(sexValue),name = info)
		# 合并两条信息
		mod2 = mod1|mod
		# 变为列表形式，免得一条数据不能迭代
		info = {'data':list(mod2)}
		return render(httpRequest,'myadmin/users/searchRes.html',info)
	elif sexValue != '-1' and (info == ""):
		print(info)
		mod = Users.objects.filter(sex = int(sexValue))
		info = {'data':list(mod)}
		return render(httpRequest,'myadmin/users/searchRes.html',info)
	elif sexValue == '-1' and info !="":
		mod = Users.objects.filter(username = info)
		mod1 = Users.objects.filter(name = info)
		mod2 = mod1|mod
		info = {'data':list(mod2)}
		return render(httpRequest,'myadmin/users/searchRes.html',info)
	else:
		# 找不到数据，随便拿一个信息过来查询，显示空
		mod = Users.objects.filter(username = info)
		return render(httpRequest,'myadmin/users/searchRes.html',info)

	
	