from django.http import HttpResponse
from django.shortcuts import render 

def home (request):
    return render(request, 'neogym-html/index.html')
def about(request):
    return render(request,'neogym-html/why.html')
def contact(request):
    return render(request,'neogym-html/contact.html')
def trainer (request):
    return render(request,'neogym-html/trainer.html')