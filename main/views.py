from django.shortcuts import render
from django.http import HttpResponse
from .forms import BranchForm

# Create your views here.
def index(request):
    if request.method=="POST":
        form=BranchForm(request.POST)
        if form.is_valid():
            new_cl=form.save()
            new_cl.save()
            return HttpResponse("зареган")
    else:
        form=BranchForm()
    return render("main/index.html",{'form':form})

