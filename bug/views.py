from django.http.request import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, 'bug.html', dict(
        range=range(1500)
    ))
