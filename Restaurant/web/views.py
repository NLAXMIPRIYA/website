from django.shortcuts import render

def home(request):
    return render(request,"home.html")
def menu(request):
    return render(request,"Menu.HTML")
def administration(request):
    return render(request,"administration.html")
def contact(request):
    return render(request,"contact.html")
