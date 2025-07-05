from django.shortcuts import render

tasks = ["clean", "groceries", "weekend-reset"]
# Create your views here.
def index(request):
    return render(request, "todo/index.html", {
        "tasks" : tasks
    })

def addTasks(request):
    return render(request, "todo/addTasks.html", {
        "tasks" : tasks
    })