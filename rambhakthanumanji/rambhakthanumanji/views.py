from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def tt(request):
    return render(request, 'tt.html')

def practise(request):
    return render(request, 'practise.html')

def out(request):
    return render(request, 'out.html')

def off(request):
    return render(request, 'off.html')

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    return render(request, 'contact.html')

def booking(request):
    return render(request, 'booking.html')

def blog(request):
    return render(request, 'blog.html')

