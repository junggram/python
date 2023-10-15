from django.db import models

# Create your models here.
class Guest(models.Model):
    #myno =models.AutoField(auto_created=True, primary_key=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    regdate=models.DateTimeField()
    
    class Meta: # 정렬을 models 에서 할수도 있음
        # ordering=('title',) title asc
        # ordering=('-title','id') title desc id asc
        ordering=('-id',) # id desc