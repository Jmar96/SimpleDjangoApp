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
    # GET  -> list every record
    # POST -> create a new record from {"name": ..., "role": ...}
    if request.method == 'GET':
        return Response(data=database.get_all())

    if request.method == 'POST':
        name = request.data.get('name')
        role = request.data.get('role')

        if not name or not role:
            return Response(data={"error": "name and role are required"}, status=400)

        new_id, record = database.create({"name": name, "role": role})
        return Response(data={"id": new_id, **record}, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
def dataDetail(request, item_id):
    # GET    -> retrieve one record
    # PUT    -> update a record from {"name": ..., "role": ...}
    # DELETE -> remove a record
    if request.method == 'GET':
        item = database.get_one(item_id)
        if item is None:
            return Response(data={"error": "Not found"}, status=404)
        return Response(data=item)

    if request.method == 'PUT':
        name = request.data.get('name')
        role = request.data.get('role')

        if not name or not role:
            return Response(data={"error": "name and role are required"}, status=400)

        updated = database.update(item_id, {"name": name, "role": role})
        if updated is None:
            return Response(data={"error": "Not found"}, status=404)
        return Response(data=updated)

    if request.method == 'DELETE':
        deleted = database.delete(item_id)
        if not deleted:
            return Response(data={"error": "Not found"}, status=404)
        return Response(data={"message": "Deleted"}, status=200)
