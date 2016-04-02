from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def hola(request):
    return HttpResponse("Hola dude this is Nacer!")