from django.shortcuts import render
from django.http import HttpResponse
from common.models import Users
import hashlib
 #引入随机函数模块
import random
from PIL import Image, ImageDraw, ImageFont
# Create your views here.
def index(httpRequest):
	return render(httpRequest,'myadmin/index.html')

# 会员登录表单
def login(httpRequest):
    return render(httpRequest,'myadmin/login.html')

# 会员执行登录
def dologin(httpRequest):
	try:
		ver1 = httpRequest.session.get("verifycode",None)
		ver2 = httpRequest.POST.get("code",None)
		del httpRequest.session['verifycode']
		#判断验证码是否错误
		if (ver1.upper() != ver2.upper()) or (ver2 == None and ver1 == None):
			data = {'info':'验证码错误'}
		else:
			uname = httpRequest.POST.get('username',None)
			# print(uname)
			# 获取username 对应的那条信息
			mod = Users.objects.get(username = uname)
			if (mod.state == 0):
				
				m = hashlib.md5()
				m.update(bytes(httpRequest.POST.get('password',None),encoding='UTF-8'))
				if (mod.password == m.hexdigest()):
					# 把当前对象的信息放入以key为adminuser 的值为 后面那个东西的值
					httpRequest.session['adminuser']=mod.toDict()
					return render(httpRequest,'myadmin/index.html')
				else:
					data = {'info':'密码错误'}

			else:
				data = {'info':"您不是管理员账户"}
			
	except Exception as e:
		# raise (e)
		data={'info':'用户不存在'}
	return render(httpRequest,'myadmin/login.html',data)
	
# 会员退出
def logout(httpRequest):
	del httpRequest.session['adminuser']
	return render(httpRequest,'myadmin/login.html')

def verify(httpRequest):

	#定义变量，用于画面的背景色、宽、高
	#bgcolor = (random.randrange(20, 100), random.randrange(
	#    20, 100),100)
	bgcolor = (242,164,247)
	width = 100
	height = 25
	#创建画面对象
	im = Image.new('RGB', (width, height), bgcolor)
	#创建画笔对象
	draw = ImageDraw.Draw(im)
	#调用画笔的point()函数绘制噪点
	for i in range(0, 100):
	    xy = (random.randrange(0, width), random.randrange(0, height))
	    fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
	    draw.point(xy, fill=fill)
	#定义验证码的备选值
	str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
	#随机选取4个值作为验证码
	rand_str = ''
	for i in range(0, 4):
	    rand_str += str1[random.randrange(0, len(str1))]
	#构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
	font = ImageFont.truetype('static/hakuyoxingshu7000.TTF', 21)
	#font = ImageFont.load_default().font
	#构造字体颜色
	fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
	#绘制4个字
	draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
	draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
	draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
	draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
	#释放画笔
	del draw
	#存入session，用于做进一步验证
	httpRequest.session['verifycode'] = rand_str
	"""
	python2的为
	# 内存文件操作
	import cStringIO
	buf = cStringIO.StringIO()
	"""
	# 内存文件操作-->此方法为python3的
	import io
	buf = io.BytesIO()
	#将图片保存在内存中，文件类型为png
	im.save(buf, 'png')
	#将内存中的图片数据返回给客户端，MIME类型为图片png
	return HttpResponse(buf.getvalue(), 'image/png')