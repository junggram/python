from django.urls import path
from myboard.views import view1, view2
urlpatterns = [ 
    
    path('list',view1.ListFunc),
    
    path('insert',view1.InsertFunc),
    path('insertok',view1.InsertOkFunc),
    
    path('search',view1.SearchFunc),
    path('content',view1.ContentFunc),
    
    path('update',view1.UpdateFunc),
    path('updateok',view1.UpdateOkFunc),
    
    path('delete',view1.DeleteFunc),
    path('deleteok',view1.DeleteOkFunc),
    
    # 답글 관련 
    path('reply',view2.replyFunc),
    path('replyok',view2.replyOkFunc),
]
