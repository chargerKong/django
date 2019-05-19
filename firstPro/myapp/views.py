from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(h):
	return HttpResponse("又一次配置")

def func1(h,num):
	return redirect(reverse('page1')) #重定向,页面跳转到page1，去路由里面找
	# return HttpResponse("func被调用，方式为'myapp/(%s)"%num)

def func2(h,num,str1):
	return HttpResponse("func被调用，方式为'myapp/(%s)/(%s)"%(num,str1))