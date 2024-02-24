from .models import  Item
from django.shortcuts import get_object_or_404 , render , redirect
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm
# Create your views here.

#render detail page with primary key
def detail(request , pk):
    item = get_object_or_404(Item , pk=pk)
    related_items = Item.objects.filter(category = item.category , is_sold = False).exclude(pk=pk)[0:3]
    return render(request , 'item/detail.html' , {'item' : item , 'related_items' : related_items})


#add new Items
@login_required
def new(request):
    if request.method == "POST" :
        form = NewItemForm(request.POST , request.FILES)
        if form.is_valid:
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail' , pk=item.id)
    form = NewItemForm()
    return render(request , 'item/new.html' , {
        'form' : form, 
    })