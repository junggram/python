from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def indexFunc(request):
    ''' 이렇게 직접 작성을 하는건 너무 비효율적이다
    msg="디장고 만세"
    ss="<html><body>장고 프로젝트 처리 %s</body></html>"%msg
    #return HttpResponse('요청 처리')
    return HttpResponse(ss)
    '''
    
    # 클라이언트에게 html파일을 반환 - 파이썬 값을 html에 담아서 전달
    msg="디장고 만세"
    a=50
    b=30
    c=115
    sum=a*b/c
    context={'msg':msg,'sum':sum} # dict type으로 작성해 html 문서에 기술한 장고 template 기호와 매칭
    
    return render(request,'main.html',context) # forward 방식이 기본

def helloFunc(request):
    
    return render(request,'show.html')















