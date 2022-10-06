from django.shortcuts import render, redirect
from .models import Infos
from infos.forms import InfosForm

# Create your views here.
def movies(request):
    info = Infos.objects.all().order_by("-id")
    context = {
        "info" : info
    }
    return render(request, 'infos/movies.html', context)


def create(request):
    if request.method == "POST":
        infos_form = InfosForm(request.POST)
        if infos_form.is_valid():
            infos_form.save()
            return redirect("infos:movies")
    else:
        infos_form = InfosForm()
    context = {
        "infos_form" : infos_form,
    }
    return render(request, 'infos/create.html', context)

def detail(request, pk):
    info = Infos.objects.get(pk=pk)
    context = {
        "info" : info,
    }
    return render(request, "infos/detail.html", context)

def delete(requst, pk):
    Infos.objects.get(pk=pk).delete()
    return redirect("infos:movies")

def update(request, pk):
    info = Infos.objects.get(pk=pk)
    
    if request.method == "POST":
        infos_form = InfosForm(request.POST, instance=info)
        if infos_form.is_valid():
            infos_form.save()
            return redirect("infos:detail", info.pk)
    else:
        infos_form = InfosForm(instance=info)
    context = {
        "infos_form" : infos_form,
        "info" : info,
    }
    return render(request, 'infos/update.html', context)