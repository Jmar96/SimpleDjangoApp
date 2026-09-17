from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path(route="todos/", view=views.todos, name="todos"),
    path("data/api/", views.getData, name="data-list"),
    path("data/api/<str:item_id>/", views.dataDetail, name="data-detail"),
]
