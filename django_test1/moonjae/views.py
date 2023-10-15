from django.shortcuts import render
from moonjae.models import Gogek, Buser, Jikwon
from datetime import datetime,date
# Create your views here.
def main(request):
    return render(request,'main.html')

def show(request):
    gogek1=Gogek.objects.get(gogek_name=request.POST.get('gname'))
    try:
        jdata=Gogek.objects.select_related('gogek_damsano').get(gogek_name=gogek1.gogek_name)
        '''name=jdata.gogek_damsano.jikwon_name
        jik=jdata.gogek_damsano.jikwon_jik
        rating=jdata.gogek_damsano.jikwon_rating
        gen=jdata.gogek_damsano.jikwon_gen
        ibsail=jdata.gogek_damsano.jikwon_ibsail
        num=jdata.gogek_damsano.buser_num''' # 이 내용을 전체를 담은게 datas
        datas=jdata.gogek_damsano
        
        day=date.today()-datas.jikwon_ibsail
        gunmu=day.days//365
        
        buser=Buser.objects.get(buser_no=datas.buser_num)
        
    except Exception as e:
        print('error: ',e)
    
    # return render(request,'show.html',{'name':name,'jik':jik,'rating':rating,'gen':gen,'bname':bname,'btel':btel,'gunmu':gunmu})
    return render(request,'show.html',{'datas':datas, 'gunmu':gunmu,'buser':buser})