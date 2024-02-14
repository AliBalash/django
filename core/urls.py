from django.urls import path

from . import views

#create a router for core and home page with name core
app_name = "core"
urlpatterns = [
    path('' , views.index , name ='index'),
    path('contact' , views.contact , name ='contact'),
    path('signup' , views.signup , name ='signup')
]