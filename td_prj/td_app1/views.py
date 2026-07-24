from django.shortcuts import render,redirect
from .forms import td_modelform
from td_app1.models import td_model

# Create your views here.
def td_views(req):
    forms = td_modelform()
    todo = td_model.objects.all()
    if req.method =="POST":
        forms = td_modelform(req.POST)
        if forms.is_valid():
            forms.save()
            return redirect(td_views)
    
    return render(req,'design.html',{"forms":forms,"todo":todo})
def td_del(req,id):
    todo = td_model.objects.get(id = id)
    if req.method == 'POST':
        todo.delete()
        return redirect(td_views)
