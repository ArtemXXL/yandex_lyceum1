from django.shortcuts import render
from django.http import HttpResponse

def item_list(request):
    return HttpResponse("<body>Список элементов</body>")

def item_detail(request, num):
    return HttpResponse(f"<body>Подробно элемент {num}</body>")