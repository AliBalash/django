from django.shortcuts import render ,redirect
from item.models import Category , Item
from .forms import SignUpForm , LoginForm
from django.contrib.auth import authenticate, login as loginUser

#render index page
def home(request): 
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    return render(request , 'core/index.html' ,{
        'items':items, 
        'categoties':categories 
    })
# render contact page html 
def contact(request): 
    return render(request , 'core/contact.html')


# signup and register user
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})
    
#signin and logi user
def login(request):
    if request.method == 'POST':
                
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('core:home')  # Redirect to the dashboard or any other page after successful login
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})
    
# def login():
    