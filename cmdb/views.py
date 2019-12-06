from django.shortcuts import render
from django.shortcuts  import HttpResponse
from cmdb import models
# Create your views here.

#文档教程来源：https://blog.csdn.net/hao65103940/article/details/79528653
user_list=[
    {"user":"jack","pwd":"abc"},
    {"user":"lilei","pwd": "ABC"},
]

def index(request):
    #return  HttpResponse("hello word")
    if request.method=="POST":
        username=request.POST.get("username",None)
        password = request.POST.get("password", None)
     #   temp={"user":username,"pwd":password}
     #   user_list.append(temp)
        #print(username,password)
    #添加数据到数据库
        models.UserInfo.objects.create(user=username,pwd=password)
    #从数据库中读取所有数据
    user_list=models.UserInfo.objects.all()
    return  render(request,"index.html",{"data":user_list})