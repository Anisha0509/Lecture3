from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path("", views.index, name = "index"),
    path("addTasks", views.addTasks, name = "addTasks"),
]