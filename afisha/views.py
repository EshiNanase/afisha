from django.http import HttpResponse


def show_phones(request):
    print('Кто-то зашёл на главную!')
    return HttpResponse('Привет!')