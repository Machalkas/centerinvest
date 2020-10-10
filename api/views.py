from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import test

def api(request):
    if request.method=='GET':
        com=request.GET.get('com','')
        if(int(com)==1):
            num=request.GET.get('n','')
            dt=test(name=int(num))
            dt.save()
            return JsonResponse({'result':'save'})
        elif(int(com)==2):
            dt=test.objects.order_by('id')
            serialized_queryset = serializers.serialize('json', dt)
            return HttpResponse(serialized_queryset)




