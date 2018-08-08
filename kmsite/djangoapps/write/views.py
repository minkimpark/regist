from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from kmsite.models import *
from django.db import connections
from django.http import HttpResponse, JsonResponse

def write(request):
    return render(request,'write/write.html')

def api_write_create(request):
    data = board(id=request.POST['id'],
                  subject=request.POST['subject'],
                  content=request.POST['content'],
                  writedate=timezone.now(),
                  hits =0
                  )
    print(data)
    data.save()

    with connections['default'].cursor() as cur:
        query = '''
            select num,id,subject,writedate,hits
            from kmsite_board;
        '''
        cur.execute(query)
        boards = cur.fetchall()

    context = {}
    context['boards'] = boards

    return render(request, 'index/index.html', context)

def api_write_read(request):
    num = request.GET['num']
    boardData = board.objects.get(num=num)
    

    context = {}
    context['num'] = boardData.num
    context['id'] = boardData.id
    context['content'] = boardData.content
    context['writedate'] = boardData.writedate
    context['hits']=boardData.hits
    print(context)

    return render(request,'write/view.html',context)

def view(request):
    return render(request,'write/view.html')
