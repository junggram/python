from django.urls import path
from gpapp import views

urlpatterns = [
    path('insert',views.insertFunc),    # funtion views
    path('insertprocess',views.insertprocessFunc),  #function views
    
    path('insert2',views.insertFunc2)
]