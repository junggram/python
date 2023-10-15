from django.shortcuts import render, redirect
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from mysurvey.models import Survey

plt.rc('font',family = 'malgun gothic')
# Create your views here.

def surveyMain(request):
    return render(request, 'main.html')

def surveyView(request):
    return render(request, 'survey.html')

def surveyProcess(request):
    insertData(request)
    return redirect('/coffee/surveyshow') # 추가후 목록 보기로 리다이렉트

def surveyAnalasis(request):
    rdata = list(Survey.objects.all().values())
    # print(rdata)
    df = pd.DataFrame(rdata)
    df.dropna()
    
    ctab=pd.crosstab(index=df['gender'],columns=df['co_survey'])
    # print(ctab)
    
    # 카이스퀘어 추정 및 검정
    chi, p, _,_ = stats.chi2_contingency(observed=ctab)
    print('chi:{},pv:{}'.format(chi,p))
    
    if p > 0.05:
        result = '유의확률이 {} > 0.05(유의수준) 이므로<br>성별과 커피브랜드의 선호도는 관계가 없다<br><strong>귀무가설을 채택</strong><br>'.format(p)
    else :
        result = '유의확률이 {} <= 0.05(유의수준) 이므로<br>성별과 커피브랜드의 선호도는 관계가 있다<br><strong>대립가설을 채택</strong><br>'.format(p)
        
    count = len(df)
    
    # 시각화 : 커피브랜드별 선호 건수에 대한 차트(세로막대)를 출력하시오.
    
    fig = plt.gcf()
    coffee_group = df.groupby(['co_survey'])['rnum'].count()
    coffee_group.plot.bar(subplots=True,color=['red','green'],width=0.5, rot=0)
    plt.xlabel('커피브랜드')
    plt.title('커피 브랜드 별 선호 건수')
    fig.savefig('django13coffee_chi/mysurvey/static/images/coffee.png')
    
    return render(request,'list.html',{'ctab':ctab.to_html(), 'result':result, 'count':count})

#------------------------------------
def insertData(request): # 설문조사 결과를 DB에 저장
    # print(request.POST.get('gender'), request.POST.get('age'), request.POST.get('co_survey'))
    if request.method=='POST' :
        Survey(
            gender = request.POST.get('gender'),
            age = request.POST.get('age'),
            co_survey = request.POST.get('co_survey')
            ).save()
            
    