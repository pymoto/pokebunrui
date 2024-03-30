from django.shortcuts import render

# Create your views here.
def indexfunc(request):
    return render(request, 'index.html', {})

def nextstationisfunc(request):
    return render(request, 'nextstationis.html', {})