from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpRequest
from models import User, Device
from django.contrib.auth import authenticate, login, logout

def index(request):
    if request.user.is_authenticated():
        return render(request,'main.html',{'user':request.user})
    else:
        return render(request,'index.html')

def getuser(request, user_id):
    try:
        u = User.objects.get(id=user_id)
        return HttpResponse(u)
    except User.DoesNotExist:
        raise Http404("User does not exist")

def  signup(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        try:
            username = request.POST.get('username')
            if User.objects.filter(username=username).exists():
                raise Http404("Username already taken!")
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            return render(request, 'main.html', {'user': user})
        except Exception, e:
            raise Http404("Something went wrong!" + str(e))

def signin(request):
    if request.user.is_authenticated():
        return render(request, 'main.html')
    else:
        if request.method == 'GET':
            return render(request,'login.html')
        elif request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,'main.html',{'user':user})
                else:
                    return HttpRequest('Sorry you account has been deactivated!')
            else:
                return render(request,'login.html',{'wrong_credentials':True})

def signout(request):
    if request.user.is_authenticated():
        logout(request)
    return render(request, 'index.html')

def username_exist(request):
    username = request.GET.get('username')
    if User.objects.filter(username=username).exists():
        return HttpResponse(1)
    return HttpResponse(0)
