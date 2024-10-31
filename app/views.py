from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETMFO=TopicModelForm()
    d={'ETMFO':ETMFO}
    if request.method=='POST':
        TMFDO=TopicModelForm(request.POST)
        if TMFDO.is_valid():
            TMFDO.save()
            return HttpResponse('Topic Created Succesfully..!')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWMFO=webpageModelForm()
    d={'EWMFO':EWMFO}
    if request.method=='POST':
        WMFDO=webpageModelForm(request.POST)
        if WMFDO.is_valid():
            WMFDO.save()
            return HttpResponse('Webpage Created Succesfully..!')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    EAMFO=AccessRecordModelForm()
    d={'EAMFO':EAMFO}
    if request.method=='POST':
        AMFDO=AccessRecordModelForm(request.POST)
        if AMFDO.is_valid():
            AMFDO.save()
            return HttpResponse('Access Record Created Succesfully..!')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_access.html',d)


def CustomizedView(request,data):
    return HttpResponse(f'Hey {data} how r u ')