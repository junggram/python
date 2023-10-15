from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from mypandas.models import Jikwon
plt.rc('font', family='malgun gothic')

def mainFunc(request):
    return render(request, 'main.html')

def showFunc(request):
    jikwons = Jikwon.objects.all().values()
    # print(jikwons)
    df=pd.DataFrame.from_records(data=jikwons)
    df.columns=['사번','직원명','부서','직급','연봉','입사','성별','평점']
    # print(df.head(2))
    
    #직급별
    jik_group = df['연봉'].groupby(df['직급'])
    # print(jik_group.sum())
    
    jik_group_detail={'연봉 합계':jik_group.sum(), '연봉 평균':jik_group.mean()} 
    df2 = pd.DataFrame(jik_group_detail)
    #print(df2)
    
    # crosstab
    ctab=pd.crosstab(df['직급'],df.성별)
    print(ctab)
    
    # 시각화
    jik_result = jik_group.agg(['sum','mean'])
    print(jik_result)
    jik_result.plot(kind='barh') # DataFrame으로 시각화를 진행
    plt.title('직급별 연봉 합 / 평균')
    plt.xlabel('연봉')
    plt.ylabel('직급')
    fig = plt.gcf() # 시각화 저장을 선언
    fig.savefig('django12_pandas/mypandas/static/images/jik.png') # 꼭!!! 절대 경로를 써줘야함 # 프로젝트명부터 쓰면됨
    
    return render(request,'list.html', {'datas':df.to_html(index=False, border=1),
                                        'jik_group':jik_group,
                                        # 'jik_group2':jik_group.to_html() #  SeriesGroupBy' object has no attribute 'to_html
                                        'jik_group_detail':df2.to_html(), # corsstab과 DataFrame만 tp_html()로 넘길 수 있다
                                        'ctab':ctab.to_html()
                                        }) # DataFrame 을 넘길 때 to_html()