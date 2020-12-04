from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def forms(request):
    if request.method == "POST":
        name = request.POST.get("name")
        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>Hello, {0}</h2>".format(name))
    else:
        userform = UserForm()
        return render(request, "forms.html", {"form": userform})