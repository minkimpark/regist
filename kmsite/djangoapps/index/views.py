from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

def index(request):

    with connections['default'].cursor() as cur:
        query = '''
            select num,id,subject,writedate,hits
            from kmsite_board;
        '''
        cur.execute(query)
        boards = cur.fetchall()
    context = {}
    context['boards'] = boards
    print(context)
    return render(request, 'index/index.html', context)
