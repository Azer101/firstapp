from django.shortcuts import render

# Create your views here.
def First(request):
    return render(request, 'first_site.html', {})