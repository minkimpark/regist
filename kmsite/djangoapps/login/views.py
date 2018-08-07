from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from kmsite.models import *

def login(request):
    return render(request,'login/login.html')

def login_check(request):
    id=request.POST['id']
    password = request.POST['password']

    print(id)
    print(password)

    data = member.objects.filter(id=id, password=password)
    print(data)
    if len(data) == 0:
        return JsonResponse({'return':'fail'})
    else:
        request.session['id'] = data[0].id
        print(request.session['id'])
        return JsonResponse({'return':'success'})

def logout(request):
    csrfmiddlewaretoken=request.POST['csrfmiddlewaretoken']
    print(csrfmiddlewaretoken)

    if 'id' in request.session:
        del request.session['id']

    return JsonResponse({'return':'success'})
