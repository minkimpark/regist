from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from kmsite.models import *

def regist(request):
    return render(request,'regist/regist.html')

def api_regist_create(request):
    id=request.POST['id']
    password = request.POST['password']
    name = request.POST['name']
    email = request.POST['email']

    data = member(id=id,password=password,name=name,email=email)
    print(data)
    data.save()

    return JsonResponse({'return':'ok'})
