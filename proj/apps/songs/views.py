from django.shortcuts import render

# Create your views here.


def index(request):
    if request.method == "POST":
        pass

    return render(request, "index.html", context={})