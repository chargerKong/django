from django.shortcuts import render
from django.http import HttpResponse
from common.models import Types
# Create your views here.
def index(httpRequest):
	'''浏览信息'''
	mod = Types.objects.extra(select={'_has':"concat(path,id)"}).order_by('_has')
	for ob in mod:
		ob.pname = " . . . "*(ob.path.count(',')-1)
	data = {"data":mod}
	return render(httpRequest,'myadmin/typesGood/index.html',data)

def add(httpRequest,pid=0):
	'''加载添加页面'''
	if pid == '0':
			path = "0,"
			name='根类别'
	else:
		ob = Types.objects.get(id=pid)
		path = ob.path+str(ob.id)+","
		name = ob.name
	data = {"pid":pid,'path':path,'name':name}
	date = {"data":data}
	return render(httpRequest,'myadmin/typesGood/add.html',date)

def insert(httpRequest):
	'''执行添加'''
	try:
		mod = Types()
		mod.name = httpRequest.POST.get('name',None)
		
		
		mod.pid = httpRequest.POST.get('pid',None)
		
		mod.path = httpRequest.POST.get('path',None)
		mod.save()
		data = {"info":'添加成功'}

	except Exception as e:
		print(e)
		data = {"info":'添加失败'}
	# return HttpResponse(mod.sex)

	return render(httpRequest,'myadmin/info.html',data)

def delete(httpRequest,uid):
	'''删除信息'''
	try:
		mod = Types.objects.get(id = uid)
		modAll = Types.objects.all()
		for ob in modAll:
			if ob.path.find(str(mod.id))!=-1:
				data = {"info":"此类别下有子类别，无法删除"}
				return render(httpRequest,'myadmin/info.html',data)
		mod.delete()
		data = {"info":'删除成功'}	

	except Exception as e:
		raise(e)
		data = {"info":'添加失败'}

	return render(httpRequest,'myadmin/info.html',data)


def edit(httpRequest,uid):
	'''加载编辑信息页面'''
	try:
		mod = Types.objects.get(id = uid)
		data = {"data":mod}
		return render(httpRequest,'myadmin/typesGood/edit.html',data)
	except Exception as e:
		print(e)
		data = {"info":'加载失败，请联系管理员'}
		return render(httpRequest,'myadmin/info.html',data)
	

def update(httpRequest,uid):
	'''执行编辑更新信息'''
	try:
		mod = Types.objects.get(id=uid)
		# mod.username = httpRequest.POST.get('username',None)
		mod.name = httpRequest.POST.get('name',None)
		
		mod.save()
		data = {"info":'修改成功'}

	except Exception as e:
		print(e)
		data = {"info":'修改失败'}
	# return HttpResponse(mod.sex)

	return render(httpRequest,'myadmin/info.html',data)