from django.shortcuts import render


def library_home_view(request):
    return render(request, 'library/library_home.html')
