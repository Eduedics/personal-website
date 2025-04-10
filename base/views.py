from django.shortcuts import render
from .models import Tag,Projects,description

# Create your views here.

def Homepage(request):
    tag = Tag.objects.all()
    context ={
        'tag':tag
    }
    return render(request,'base/home.html',context=context)
