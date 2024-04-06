from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':20,'b':45,'c':50}
    return render(request,'condition.html',context=d)
def loop(request):
    d={'name':'Krishnamohan'}
    return render(request,'condition.html',d)