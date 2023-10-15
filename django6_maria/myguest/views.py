from django.shortcuts import render, redirect
from myguest.models import Guest
from datetime import datetime
from django.utils import timezone
from django.http.response import HttpResponseRedirect
# Create your views here.
def MainFunc(request):
    msg = "<h1>홈페이지</h1>"
    return render(request, 'main.html', {'msg':msg})

def ListFunc(request):
    #gdatas = Guest.objects.all() # ORM
    #print(gdatas)
    #print(Guest.objects.get(id=1)) # 자료를 받아서 출력
    #print(Guest.objects.filter(id=1)) #자료를 id번호로 필터해서 출력
    #print(Guest.objects.filter(title='내일')) #자료를 문자열로 필터해서 출력

    gdatas = Guest.objects.all()
    
    #정렬
    # gdatas = Guest.objects.all().order_by('title') # asc 오름차순
    # gdatas = Guest.objects.all().order_by('-title') # desc 내림차순
    # gdatas = Guest.objects.all().order_by('-id')
    # gdatas = Guest.objects.all().order_by('title','-id') # 인자로 들어간 칼럼의 순서대로 정렬 (title asc, id desc)
    # gdatas = Guest.objects.all().order_by('-id')[0:2] # 리스트의 index를 참조해서 선택한 자료만 뽑을 수 있음
    return render(request, 'list.html', {'gdatas':gdatas})

def InsertFunc(request):
    return render(request, 'insert.html')
    
def InsertOkFunc(request):
    if request.method=="POST":
        #print(request.POST['title'])
        #print(request.POST.get('title'))
        Guest(
            title=request.POST['title'],
            content=request.POST['content'],
            #regdate=datetime.now()
            regdate=timezone.now()
        ).save()
        # from datetime import datetime
        # from django.utils import timezone 을 import 해서 regdate 값을 넘겨줌
        
    # return  HttpResponseRedirect('/guest/select') # 추가 후 목록 보기
    return redirect('/guest/select') # django.shortcuts 를 import 해서 이렇게 작성할수도있다