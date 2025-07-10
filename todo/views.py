from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

from .models import Notepad

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New task")
    # priority = forms.IntegerField(label = "Priority", min_value = 1, max_value = 5)

# Create your views here.
def index(request):
    # if "tasks" not in request.session:
    #     request.session["tasks"] = []
    # return render(request, "todo/index.html", { "tasks" : request.session["tasks"] })
    tasks = Notepad.objects.all()
    return render(request, "todo/index.html", { "tasks" : tasks})

def addTasks(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            #request.session["tasks"] += [task]
            item = Notepad ( taskItem = task )
            item.save()
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request, "todo/addTasks.html", {
                "form" : form
            })
    return render(request, "todo/addTasks.html", {
        "form" : NewTaskForm()
    })