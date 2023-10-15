from django.shortcuts import render

# Create your views here.
def mainFunc(request):
    return render(request,'main.html')

def page1Func(request):
    return render(request,'page1.html')

def page2Func(request):
    return render(request,'page2.html')

def cartFunc(request):
    name=request.POST["name"] 
    price=request.POST["price"]
    product= {'name':name, 'price':price}
    
    productList=[]
    
    if "shop" in request.session:
        productList=request.session['shop']     # 세션(냉장고)내에 shop이라는 키로 등록이 되어있는 productList(김밥통) 을 꺼낸다
        productList.append(product)     # productList(김밥통)에 product(김밥)을 넣고
        request.session['shop']=productList     # productList(김밥통) 을 shop이라는 키로 세션(냉장고)에 넣음
    else:
        productList.append(product)             # 첫번째 상품은 김밥통이 없으니까 김밥통에 상품을 넣고
        request.session['shop']=productList     # 김밥통을 냉장고에 넣는다
    print(productList)
    context={}
    context['products']=request.session['shop']
    return render(request,'cart.html',context)


def buyFunc(request):
    if "shop" in request.session:
        productList=request.session['shop']
        total=0
        
        for p in productList:
            total+=int(p['price'])
            
        print('결제 총액: ',total)
        request.session.clear() # 세션 내의 모든 키 삭제
        # del request.session['shop'] # 특정 키를 가진 세션 내용 삭제
        
    return render(request,'buy.html',{'total':total})