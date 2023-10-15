from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def mainFunc(request):
    return render(request,'index.html')

class CallView(TemplateView):   #django.views.generic.base의 TemplateView
    template_name="callget.html"
    
def insertFunc(request):
    return render(request,'insert.html')

def insertprocessFunc(request):
    if request.method=='GET':
        irum=request.GET.get("name") # java : request.getparameter("name")
        print(irum)
        return render(request,'list.html',{'myname':irum})
    
def insertFunc2(request):
    if request.method=='GET': 
        return render(request,'insert2.html')
    elif request.method=='POST':  
        irum=request.POST.get("name")
        return render(request,'list.html',{'myname':irum})
    else:
        print('요청 에러')