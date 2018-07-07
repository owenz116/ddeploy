from django.shortcuts import render
from basicapp.forms import Userform,UPIform
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request,'bapp/I.html')
@login_required
def ulogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def ulogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print('login failed!')
            print(username,password)
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request,'bapp/L.html')
def register(request):
    registered = False
    if request.method == 'POST':
        uf = Userform(data=request.POST)
        pf = UPIform(data=request.POST)
        if uf.is_valid() and pf.is_valid():
            user = uf.save()
            user.set_password(user.password)
            user.save()
            profile = pf.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(uf.errors,pf.errors)
    else:
        uf = Userform()
        pf = UPIform()
    D = {'userform':uf,'profileform':pf,'registered':registered}
    return render(request,'bapp/R.html',D)
