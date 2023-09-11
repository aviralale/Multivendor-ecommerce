from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm
from item.models import Category
from django.db.models import Q

# Create your views here.
def detail(request, pk):
    categories = Category.objects.all()
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold = False).exclude(pk=pk)[:3]
    context = {
        'item':item,
        'related_items': related_items,
        'categories': categories,
    }
    return render(request,'item/detail.html',context)

@login_required
def newItem(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail',pk=item.id)
    else:
        form = NewItemForm()
    context = {
        'form': form,
        'title': 'New Item',
        'categories': categories,
    }
    return render(request, 'item/form.html', context)

@login_required
def editItem(request, pk):
    categories = Category.objects.all()
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail',pk=item.id)
    else:
        form = EditItemForm(instance=item)
    context = {
        'form': form,
        'title': 'Edit Item',
        'categories': categories,
    }
    return render(request, 'item/form.html', context)

@login_required
def delete(request, pk):
    categories = Category.objects.all()
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    context = {
        'categories': categories,
    }
    return redirect('dashboard:index',context)

def items(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category',0)
    items = Item.objects.filter(is_sold=False)

    query = request.GET.get('query', '')

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(
        Q(name__icontains=query) | Q(description__icontains=query)  
        )
    context = {
        'items':items,
        'categories': categories,
        'query': query,
        'category_id': int(category_id),
    }
    return render(request, 'item/browser.html', context)