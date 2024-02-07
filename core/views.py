from django.shortcuts import render 

# Create your views here. 
def index(request): 
    return render(request , 'core/index.html') 
# render contact page html 
def contact(request): 
    return render(request , 'core/contact.html')