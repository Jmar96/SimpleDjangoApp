from django.shortcuts import render, HttpResponse
from .models import TodoItem
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .import database


# Create your views here.
def home(request):
    return render(request=request, template_name="home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request=request, template_name="todos.html", context={"todos": items})

@api_view(['GET', 'POST'])
def getData(request):
    data = database.myData
    return Response(data=data)