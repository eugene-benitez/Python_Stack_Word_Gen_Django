from django.shortcuts import render, HttpResponse, redirect

from django.utils.crypto import get_random_string


def index(request):
    request.session['counter'] = 0
    return render(request, "word_random/index.html")

def add(request):
    request.session['counter'] += 1
    r_string = get_random_string(length=14)
    context = {
        "count": request.session['counter'],
        "string": r_string,
    }
    return render(request, "word_random/index.html", context)


def clear(request):
    request.session['counter'] = 0
    r_string = get_random_string(length=14)
    context = {
        "count": request.session['counter'],
        "string": r_string,
    }
    return render(request, "word_random/index.html", context)
