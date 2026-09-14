from django.shortcuts import render, HttpResponse
from .models import TodoItem


# Create your views here.
def home(request):
    return render(request=request, template_name="home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request=request, template_name="todos.html", context={"todos": items})