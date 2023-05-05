from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
from django.core.mail import send_mail
def registation(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            nsuo=ufd.save(commit=False)
            nsuo.set_password(ufd.cleaned_data['password'])
            nsuo.save()
            nspo=pfd.save(commit=False)
            nspo.username=nsuo
            nspo.save()

            send_mail('Registratioon',
                      "Succefully Registration is Done",
                      'azeembasha9090@gmail.com',
                      [nsuo.email],
                      fail_silently=False

                      )


            
            return HttpResponse('DATA IS VALID')
        else:
            return HttpResponse('data is not valid')
    return render(request,'registation.html',d)