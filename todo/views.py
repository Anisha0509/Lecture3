from django.shortcuts import render
from django import forms

tasks = ["clean", "groceries", "weekend-reset"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New task")
    # priority = forms.IntegerField(label = "Priority", min_value = 1, max_value = 5)

# Create your views here.
def index(request):
    return render(request, "todo/index.html", {
        "tasks" : tasks
    })

def addTasks(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return render(request, "todo/index.html", {
                "tasks" : tasks
            })
        else:
            return render(request, "todo/addTasks.html", {
                "form" : form
            })
    return render(request, "todo/addTasks.html", {
        "form" : NewTaskForm()
    })