from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
	return Httpresponse('hello world')


def login(request):
    return redirect('www.baidu.com')
