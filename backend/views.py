from django.http import HttpResponse


def simpleResponse(request):
    return HttpResponse('<h1>This is my first django response</h1>')