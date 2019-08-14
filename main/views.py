from django.shortcuts import redirect, get_object_or_404, render

def home(request):
    return render(request, 'main/home.html', locals())

