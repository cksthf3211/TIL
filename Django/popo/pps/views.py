from django.shortcuts import render, redirect
from .models import Article
from .forms import PpsForm

# Create your views here.

def index(request):
    pps = Article.objects.order_by('-pk')
    context = {
        'pps' : pps,
    }
    return render(request, 'pps/index.html', context)

# def new(request):
#     pps_Form = PpsForm()
#     context = {
#         'pps_Form' : pps_Form
#     }
#     return render(request, 'pps/new.html', context)


def create(request):
    if request.method == 'POST':
        pps_Form = PpsForm(request.POST)
        if pps_Form.is_valid():
            pps_Form.save()
            return redirect('pps:index')
    else:
        pps_Form = PpsForm()
    context = {
        'pps_Form' : pps_Form,
    }
    return render(request, 'pps/new.html', context)


def detail(request, pk):
    pps = Article.objects.get(pk=pk)
    context = {
        'pps' : pps,
    }
    return render(request, 'pps/detail.html', context)


def update(request, pk):
    pps = Article.objects.get(pk=pk)
    if request.method == 'POST':
        pps_Form = PpsForm(request.POST, instance=pps)
        if pps_Form.is_valid():
            pps_Form.save()
            return redirect('pps:detail', pps.pk)
    else:
        pps_Form = PpsForm(instance=pps)
    context = {
        'pps_Form' : pps_Form
    }
    return render(request, 'pps/update.html', context)