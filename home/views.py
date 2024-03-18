from django.shortcuts import render
from django.views import View
from . models import home,homess,introduction,about,cart,review,cv,number,sent
from django.contrib import messages

def iintroduction(request):
    intitr=introduction.objects.all()
    ab=about.objects.all()
    ct=cart.objects.all()
    rv=review.objects.all()
    nm=number.objects.all()
    if request.method=='POST':
        sen=sent()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        sen.name=name
        sen.email=email
        sen.subject=subject
        sen.save()
        messages.success(request,'Successfuly Sent')
    return render(request,'home/index.html',{'intri':intitr,'abou':ab,'cart':ct,'r':rv,'n':nm})

def aboutt(request):
    ab=about.objects.all()
    ct=cart.objects.all()
    return render(request,'home/index.html',{'abou':ab,'cart':ct})

def cartt(request):
    ct=cart.objects.all()
    return render(request,'home/index.html',{'cart':ct})

def ra(request):
    ct=cart.objects.all()
    return render(request,'home/index.html',{'cart':ct})

def cve(request):
    cvt=cv.objects.all()
    return render(request,'home/index.html',{'cv':cvt})

def reviews(request):
    rv=review.objects.all()
    return render(request,'home/index.html',{'review':rv})
