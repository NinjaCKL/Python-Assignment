from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mypagefunction(request):
    return HttpResponse('<h1>Welcome to my page</h1>')
def contactfunction(request):
    return render(request, 'contact_page.html')