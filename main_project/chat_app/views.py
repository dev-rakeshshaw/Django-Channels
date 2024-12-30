from django.shortcuts import render

def index(request, group_name):
    return render(request,'chat_app/index.html', {"group_name":group_name})
