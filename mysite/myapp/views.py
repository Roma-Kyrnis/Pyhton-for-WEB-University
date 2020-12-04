from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def forms(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            email = userform.cleaned_data["Email"]
            password = userform.cleaned_data["Password"]
            return HttpResponse("<h2>Hello our client. You enter in net Bank. Your Email: {0} and Password: {1}</h2>".format(email, password))
        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm()
        return render(request, "forms.html", {"form": userform})
