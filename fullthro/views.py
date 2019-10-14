from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    word = request.GET.get('word')
    if word:
        context = {
            'word' : word,
        }
        return JsonResponse(context)
    else:
        return render(request, 'index.html')
        