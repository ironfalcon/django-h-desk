from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


# Create your views here.
def kek(request):
    return render(request, 'mainApp/kek.html', {'keki': ['kek1', 'kek2',
                                                         'kek3', 'kek4', 'kek5']})
