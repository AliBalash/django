from django.urls import path
from . import views


#create a router for items with name item
app_name = "item"
urlpatterns = [
    path('<int:pk>/' ,views.detail , name='detail')

]