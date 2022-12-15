from django.shortcuts import render


def custom_404_error(request, exception):
    return render(request, 'errors/404.html')


def custom_403_error(request, exception):
    return render(request, 'errors/403.html')
