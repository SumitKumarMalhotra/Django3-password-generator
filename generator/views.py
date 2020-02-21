from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html',{'password':'hello'})
    #return HttpResponse('hello')

def password(request):

    clist=list('abcdefghijklmnopqrstuvwxyz')
    ulist=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    slist=list('!@#$%^&*()_+')
    nlist=list('0123456789')


    if request.GET.get('uppercase'):
        clist.extend(ulist)


    if request.GET.get('special'):
            clist.extend(slist)

    if request.GET.get('numbers'):
            clist.extend(nlist)


    length=int(request.GET.get('length',12))

    thepassword=''
    for x in range(length):
        thepassword += random.choice(clist)

    return render(request,'generator/password.html',{'password':thepassword})
    #return HttpResponse('hello')



def about(request):
    return render(request,'generator/about.html')
