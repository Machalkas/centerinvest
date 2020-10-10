from django.shortcuts import render
from django.http import HttpResponse
from .forms import QueueForm
from .models import Queue
from django import forms
# Create your views here.
def index(request):
    if request.method=="POST":
        form=QueueForm(request.POST)
        if form.is_valid():
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
            new_cl=form.save()
            new_cl.number=q_num
            new_cl.save()
            return HttpResponse(q_num)
    else:
        form=QueueForm()
        form.fields['number'].widget = forms.HiddenInput()
    return render(request, "main/index.html",{'form':form})

