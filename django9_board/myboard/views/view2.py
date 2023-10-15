from django.shortcuts import render, redirect
from myboard.models import BoardTab
from datetime import datetime
# Create your views here.
def replyFunc(request):
    try:
        data=BoardTab.objects.get(id=request.GET.get('id'))
        context={'data_one':data}
        return render(request,'reply/reply.html',context)
    except Exception as e:
        print('replyFunc err : ',e)
        return render(request,'error.html')

def replyOkFunc(request):
    if request.method=="POST":
        try:
            repGnum=int(request.POST.get('gnum'))
            repOnum=int(request.POST.get('onum'))
            imsiRec=BoardTab.objects.get(id=request.POST.get('id'))
            oldGnum=imsiRec.gnum
            oldOnum=imsiRec.onum
            
            if oldGnum==repGnum:
                oldOnum=oldOnum+1  # if문을 써서 조금더 보완이 필요함
            
            # 답글 저장
            BoardTab(
                name=request.POST.get('name'),
                passwd=request.POST.get('passwd'),
                mail=request.POST.get('mail'),
                title=request.POST.get('title'),
                cont=request.POST.get('cont'),
                bip=request.META['REMOTE_ADDR'], # 요청한 클라이언트의 컴퓨터 주소 (글을 입력한 컴퓨터의 주소)
                bdate=datetime.now(),
                readcnt=0,
                gnum=repGnum,
                onum=oldOnum,
                nested=int(request.POST.get('nested'))+1
            ).save()
                    
            return redirect('/board/list') # 답글 작성 후 목록보기
        except Exception as e:
            print('replyOkFunc err : ',e)
            return render(request,'error.html')