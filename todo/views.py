from django.shortcuts import render
from .models import Item

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items' : items, 
        'title2': "<h2> estoy enviando un string</h2>"
    }
    # context = {
    #     'title2' : "<h2> estoy enviando un string</h2>"
    # }
    return render(request, 'todo/todo_list.html', context)