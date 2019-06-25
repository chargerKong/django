from django.shortcuts import render
from django.http import HttpResponse
from common.models import Goods,Types
from django.core.paginator import Paginator
import time,os
from PIL import Image
from django.db.models import Q

# Create your views here.
def index(httpRequest,pindex=1):
	'''浏览信息'''
	mod = Goods.objects.all()
	# 储存查询信息，用于状态维持
	where=[]
	print(mod)
	# 条件查询部分、
	search = httpRequest.GET.get("search",None)

	if search:
		
		mod = mod.filter(goods = (search.strip()))
		
		where.append("search="+search)
	# 商品的大类别在typeid 中是没有的，比如食品。
	# 先找到所有路径含有食品的id, 然后利用此作为typeid 去Goods里面找
	typeie = httpRequest.GET.get('type',None)


	if typeie is not None and typeie != '-1':
		# temp = mod.filter(typeid=typeie)
		# if not temp:
		# 把id 为type 和 path包含type的放在一起，提取id 
		value = Types.objects.filter(Q(id=typeie)|Q(path__contains=typeie)).values_list("id")
		mod = mod.filter(typeid__in=value)
		# else:
			# mod = temp
		where.append("type="+typeie)
	state = httpRequest.GET.get('select',None)
	if state is not None and state != '-1':
		mod = mod.filter(state = state)
		where.append("select="+state)

	where = "&".join(where)

	# 先筛选在加名字
	for i in mod:
		i.name = Types.objects.get(id = i.typeid).name 
	# 加一个类别选择项
	mod2 = Types.objects.extra(select={'_has':"concat(path,id)"}).order_by('_has')
	for i in mod2:
		i.pname = ". . ."*(i.path.count(",")-1)	


	p = Paginator(mod,2)#两条一页
	
	list2 = p.page(pindex) #拿取第pindex页的数据
	list3 = p.page_range
	if (len(list3))==1:
		nextPage = pindex
		prePage = pindex

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

	data={'typelist':mod2,"data":list2,'list3':list3,'pindex':int(pindex),'nextPage':nextPage,'prePage':prePage,'where':where}
	return render(httpRequest,'myadmin/goods/index.html', data)

def add(httpRequest):
	'''加载添加页面'''
	
	mod = Types.objects.extra(select={'_has':"concat(path,id)"}).order_by('_has')
	# 添加遍历效果的属性
	for i in mod:
		i.pname = ". . ."*(i.path.count(',')-1)
	
	list1={'data':mod}

	return render(httpRequest,'myadmin/goods/add.html',list1)

def insert(httpRequest):
	'''执行添加'''
	try:
		mod = Goods()
		mod.goods = httpRequest.POST.get('goods',None)
		mod.company = httpRequest.POST.get('company',None)
		mod.typeid = httpRequest.POST.get('typeid',None)
		mod.price = httpRequest.POST.get('price',None)
		mod.store = httpRequest.POST.get('store',None)
		mod.state = 1
		# 存图片名字，存图片
		myfile = httpRequest.FILES.get('picname',None)
		if not myfile:
			return HttpResponse("没有上传文件信息")
		filename = str(time.time())+"."+myfile.name.split('.').pop()
		destination = open("./static/pics/"+filename,"wb+")
		for chunk in myfile.chunks():      # 分块写入文件  
			destination.write(chunk)  
			destination.close()

			# 执行图片缩放
		im = Image.open("./static/pics/"+filename)
		# 缩放到75*75(缩放后的宽高比例不变):
		im.thumbnail((75, 75))
		# 把缩放后的图像用jpeg格式保存: 
		im.save("./static/pics/s75_"+filename,None)

		im = Image.open("./static/pics/"+filename)
		# 缩放到75*75(缩放后的宽高比例不变):
		im.thumbnail((225, 225))
		# 把缩放后的图像用jpeg格式保存: 
		im.save("./static/pics/s225_"+filename,None)

		#执行图片删除
		#os.remove("./static/pics/"+filename)
		mod.picname = filename
		mod.content = httpRequest.POST.get('content',None)
		mod.clicknum = 0
		mod.save()
		data = {"info":'添加成功'}

	except Exception as e:
		print(e)
		data = {"info":'添加失败'}
		return render(httpRequest,'myadmin/info.html',data)

	return render(httpRequest,'myadmin/info.html',data)

def delete(httpRequest,uid):
	'''删除信息'''
	try:
		mod = Goods.objects.get(id = uid)
		if mod.state !='0':
			data = {"info":"删除的商品只能为新商品"}
			return render(httpRequest,'myadmin/info.html',data)
		
		try:
			os.remove("./static/pics/"+filename)
		except:
			pass
		try:
			os.remove("./static/pics/s75_"+filename)
		except:
			pass
		try:
			os.remove("./static/pics/s225_"+filename)
		except:
			pass
		mod.delete()
		data = {"info":'添加成功'}

	except Exception as e:
		print(e)
		data = {"info":'添加失败'}
	return render(httpRequest,'myadmin/info.html',data)


def edit(httpRequest,uid):
	'''加载编辑信息页面'''
	try:
		mod = Goods.objects.get(id = uid)
		data = {"data":mod}
		return render(httpRequest,'myadmin/goods/edit.html',data)
	except Exception as e:
		print(e)
		data = {"info":'加载失败，请联系管理员'}
		return render(httpRequest,'myadmin/info.html',data)
	

def update(httpRequest,uid):
	'''执行编辑更新信息'''
	try:
		mod = Goods.objects.get(id=uid)
		mod.goods = httpRequest.POST.get('goods',None)
		mod.company = httpRequest.POST.get('company',None)
		
		mod.price = httpRequest.POST.get('price',None)
		mod.store = httpRequest.POST.get('store',None)
		# 存图片名字，存图片
		myfile = httpRequest.FILES.get('picname',None)
		if not myfile:
			pass
		else:
			filename = mod.picname;
			try:
				os.remove("./static/pics/"+filename)
				os.remove("./static/pics/s75_"+filename)
				os.remove("./static/pics/s225_"+filename)
			except Exception as e:
				pass
			
			filename = str(time.time())+"."+myfile.name.split('.').pop()
			destination = open("./static/pics/"+filename,"wb+")
			for chunk in myfile.chunks():      # 分块写入文件  
				destination.write(chunk)  
				destination.close()

				# 执行图片缩放
			im = Image.open("./static/pics/"+filename)
			# 缩放到75*75(缩放后的宽高比例不变):
			im.thumbnail((75, 75))
			# 把缩放后的图像用jpeg格式保存: 
			im.save("./static/pics/s75_"+filename,None)

			im = Image.open("./static/pics/"+filename)
			# 缩放到75*75(缩放后的宽高比例不变):
			im.thumbnail((225, 225))
			# 把缩放后的图像用jpeg格式保存: 
			im.save("./static/pics/s225_"+filename,None)

			#执行图片删除
		#os.remove("./static/pics/"+filename)
			mod.picname = filename
		mod.content = httpRequest.POST.get('content',None)
		mod.state = httpRequest.POST.get('state',None)
		mod.clicknum = httpRequest.POST.get('clicknum',None)
		# print(mod.price)
		mod.save()
		data = {"info":'修改成功'}

	except Exception as e:
		print(e)
		data = {"info":'修改失败'}
		return render(httpRequest,'myadmin/info.html',data)

	return render(httpRequest,'myadmin/info.html',data)

def editPaw(httpRequest,uid):
	try:
		mod = Goods.objects.get(id=uid)
		data = {"id":uid,"name":mod.name,"username":mod.username}
		date = {"data":data}
		return render(httpRequest,'myadmin/Goods/editPaw.html',date)
	except Exception as e:
		raise(e)
		data = {"info":'信息获取错误'}
		return render(httpRequest,'myadmin/info.html',data)
	

def chanPaw(httpRequest,uid):
	try:
		mod = Goods.objects.get(id=uid)
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
		mod = Goods.objects.filter(sex = int(sexValue),username = info)
		mod1 = Goods.objects.filter(sex = int(sexValue),name = info)
		# 合并两条信息
		mod2 = mod1|mod
		# 变为列表形式，免得一条数据不能迭代
		info = {'data':list(mod2)}
		return render(httpRequest,'myadmin/Goods/searchRes.html',info)
	elif sexValue != '-1' and (info == ""):
		print(info)
		mod = Goods.objects.filter(sex = int(sexValue))
		info = {'data':list(mod)}
		return render(httpRequest,'myadmin/Goods/searchRes.html',info)
	elif sexValue == '-1' and info !="":
		mod = Goods.objects.filter(username = info)
		mod1 = Goods.objects.filter(name = info)
		mod2 = mod1|mod
		info = {'data':list(mod2)}
		return render(httpRequest,'myadmin/Goods/searchRes.html',info)
	else:
		# 找不到数据，随便拿一个信息过来查询，显示空
		mod = Goods.objects.filter(username = info)
		return render(httpRequest,'myadmin/Goods/searchRes.html',info)
