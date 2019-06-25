from django.shortcuts import render
from django.http import HttpResponse
from common.models import Users,Types,Goods
from django.core.paginator import Paginator
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
	'''主页'''
	mod = loadinfo(httpRequest);
	mod2 = Goods.objects.all().order_by('-clicknum')
	mod['totalList'] = mod2[:5]

	# 找到数码类的信息，按照点击量排序
	mo=Types.objects.filter(path__contains=2).values_list("id")
	shuma =Goods.objects.filter(typeid__in=mo).order_by('-clicknum')
	mod['shumaList'] = shuma[:5]

	# 找到服装类信息
	mo=Types.objects.filter(path__contains=1).values_list("id")
	clothes =Goods.objects.filter(typeid__in=mo).order_by('-addtime')
	mod['clothList'] = clothes[:5]
	return render(httpRequest,"web/index.html",mod)

def list(httpRequest,pindex=1):
	'''显示各种列表页'''
	mod = loadinfo(httpRequest);
	# 获取所有的物品
	mod2 = Goods.objects.all()

	tid = httpRequest.GET.get("tid")
	mywhere = []
	if tid:
		# 先找到path中包含此类别的所有id
		mo=Types.objects.filter(path__contains=tid).values_list("id")
		
		mod2=Goods.objects.filter(typeid__in=mo)

		mywhere.append("tid="+tid)

	# 增加分页
	p = Paginator(mod2,2) #设置一页八条
	if int(pindex)>p.num_pages:
		pindex = p.num_pages
	elif int(pindex)<=0:
		pindex = 1
	plist = p.page(pindex)#拿取第pindex的数据

	mod['mywhere'] = '&'.join(mywhere)

	mod['range'] = p.page_range

	mod['pindex']=int(pindex)
	# 在原来的mod字典里新增物品的键值对
	mod['goodslist'] = plist
	return render(httpRequest,"web/list.html",mod)

def detail(httpRequest,uid):
	'''显示详情页'''
	mod = loadinfo(httpRequest);
	mod2 = Goods.objects.get(id = uid)
	mod2.clicknum +=1
	mod2.save()
	mod['goods'] = mod2
	# return render(httpRequest,"web/list.html",mod)
	return render(httpRequest,"web/detail.html",mod)

def login(httpRequest):
	'''返回登录界面'''
	return render(httpRequest,'web/login.html')

def dologin(httpRequest):
	'''执行登录'''
	very = httpRequest.POST.get('code',None)

	if very!=httpRequest.session.get('verifycode'):
		data = {"info":'验证码信息错误'}
		return render(httpRequest,'web/login.html',data)
	try:
		username = httpRequest.POST.get('username',None)
		print(username)
		mod = Users.objects.get(username=username.strip())
		if mod.state == 1:
			m = hashlib.md5()
			m.update(bytes(httpRequest.POST.get('password'),encoding='utf8'))
			if m.hexdigest() == mod.password:
				# 写入session 值
				httpRequest.session['vipuser'] = mod.toDict()	
				return redirect(reverse('index'))
			else:
				data = {"info":'密码错误'}

		else:
			data = {"info":'账户被禁用'}
			# return render(httpRequest,"web/meilanx.html",data)
	except Exception as e:
		print(e)
		data = {"info":'没有此用户'}
	return render(httpRequest,'web/login.html',data)
	

	return render(httpRequest,"web/meilanx.html")
def logout(httpRequest):
	# print(httpRequest.session['vipuser'])
	# 删除session中的值
	del httpRequest.session['vipuser']

	return render(httpRequest,"web/login.html")
	# return redirect(reverse('login'))


def registor(httpRequest):
	return render(httpRequest,"web/registor.html")

def insert(httpRequest):
	'''信息注册'''
	very = httpRequest.POST.get('code',None)

	if very!=httpRequest.session.get('verifycode'):
		data = {"info":'验证码信息错误'}
		return render(httpRequest,'web/registor.html',data)
	try:
		mod = Users()
		username = httpRequest.POST.get('username',None)
		name = httpRequest.POST.get('name',None)
		psd = httpRequest.POST.get('password',None)

		if (not username) or (not 	name) or (not psd):
			data = {"info":'请把信息填写完整'}
			return render(httpRequest,'web/registor.html',data)
		psd1 = httpRequest.POST.get('password1',None)
		if psd != psd1:
			data = {"info":'密码输入不一致'}
			return render(httpRequest,'web/registor.html',data)
		#获取密码并md5	
		m = hashlib.md5() 
		m.update(bytes(psd,encoding="utf8"))
		mod.password = m.hexdigest()
		mod.username  = username
		mod.name = name
		mod.sex = httpRequest.POST.get('sex',"-1")
		mod.address = httpRequest.POST.get('address',"")
		mod.phone = httpRequest.POST.get('phone',"")
		mod.email = httpRequest.POST.get('email',"")
		mod.state = 1
		mod.code = ""
		mod.save()
		data = {"info":'注册成功'}
		
	except Exception as e:
		print(e)
		data = {"info":'账号已被注册添加！'}
		return render(httpRequest,'web/registor.html',data)

	return render(httpRequest,'web/registor.html',data)



