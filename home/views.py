from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
   # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')

def services(request):
    return HttpResponse("this is services page")

def contacts(request):
    return render(request, 'contacts.html')

