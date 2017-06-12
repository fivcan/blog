from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from models import *
from markdown import markdown


def index(request):
    essays = EssayInfo.objects.all().order_by('-time')[:10]
    return render(request, 'essay/index.html', {'essays': essays})

def ajax_index(request):
    essays = EssayInfo.objects.all().order_by('-time')[10:]
    data = []
    for i in essays:
        data.append({'title': i.title, 'time': i.time, 'content': i.content, 'id': i.id})
    data = {'data': data}
    return JsonResponse(data)

def md2html(mdstr):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
    html = '''
    <html lang="zh-cn">
    <head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    <link href="/static/css/default.css" rel="stylesheet">
    <link href="/static/css/github.css" rel="stylesheet">
    </head>
    <body>
    %s
    </body>
    </html>
    '''
    ret = markdown(mdstr,extensions=exts)
    return html % ret


def detail(request):
    id = request.GET.get('id', '')
    if id:
        essay = EssayInfo.objects.get(id=int(id))
        content = md2html(essay.content)
        return HttpResponse(content)
    else:
        return HttpResponse('Essay is not Found')

def about(request):
    return render(request, 'essay/about.html')
def post(request):
    return render(request, 'essay/post.html')
def contact(request):
    return render(request, 'essay/contact.html')

def send(request):
    contactor = ContactInfo()
    contactor.user = request.POST.get('user')
    contactor.email = request.POST.get('email')
    contactor.phone = request.POST.get('phone')
    contactor.content = request.POST.get('content')
    contactor.save()
    context = {'is_send': True}
    response = render(request, 'essay/contact.html', context)

    return response