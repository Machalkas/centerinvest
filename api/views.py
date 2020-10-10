from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from .models import test
from main.models import Branch, Services, Queue

def api(request):
    if request.method=='GET':
        com=request.GET.get('com','')
        if(int(com)==1):
            num=request.GET.get('n','')
            dt=test(name=int(num))
            dt.save()
            return JsonResponse({'result':'save'})
        elif(int(com)==2):
            # dt=test.objects.order_by('id')
            # serialized_queryset = serializers.serialize('json', dt)
            x=test.objects.all()
            # print(type(x.values('name')))
            # data=serialize('json', test.objects.all())
            return HttpResponse(x.values('name'))
def a(request):
    if request.method=='GET':
        br=Branch.objects.all()
        st=Services.objects.all()
        qe=Queue.objects.all()
        op=request.GET.get('oper','')
        if op=="otdel":
            return HttpResponse(br.values('id', 'name', 'addres', 'discript'))
        elif op=="uslugi":
            return HttpResponse(st.values('id','name', 'window', 'branch'))
        elif op=="ochered":
            return HttpResponse(qe.values('time', 'service', 'branch', 'number', 'is_active'))
        elif op=="edit":
            time=request.GET.get('time','')
            banch=request.GET.get('otdel','')
            service=request.GET.get('service','')

            q=Queue.objects.all().order_by('id')
            last_num=None
            for i in range(len(q)-1,-1,-1):
                if q[i].is_active==True:
                    last_num=q[i].number
                    break
            if last_num==None:
                q_num="I0"
            else:
                last_num=last_num[1:]
                q_num="I"+str(int(last_num)+1)
            Sobj,created = Services.objects.get_or_create(id=int(service))
            Bobj,created = Branch.objects.get_or_create(id=int(banch))
            dt=Queue(time=time, service=Sobj, branch=Bobj, number=q_num, is_active=True)
            dt.save()
            return JsonResponse({'number':q_num})

            
    




