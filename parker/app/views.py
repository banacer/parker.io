from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpRequest
from models import User, Device


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def hola(request):
    return HttpResponse('Hola it\' nacer')
def getuser(request,user_id):
    try:
        u = User.objects.get(id = user_id)
        return HttpResponse(u)
    except User.DoesNotExist:
        raise Http404("User does not exist")
def signup(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        try:
            username = request.POST.get('username')
            if User.objects.filter(username=username).exists():
                raise Http404("Username already taken!")
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User(first_name = fname, last_name = lname,email = email,username = username )
            user.set_password(password)
            user.save()
            return HttpResponse('You are signed up dear '+user.first_name)
        except Exception,e:
            raise Http404("Something went wrong!" + str(e))

