from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.

def index(request):
    k = Review.objects.all().order_by("-id")
    context = {
        "v" : k
    }
    return render(request, "ppaps/index.html", context)

def create(request):
    # if request.method == "GET":
    #     k = request.GET
    #     v = [k[i] for i in k]
    #     context = {
    #         "v" : v,
    #     }
    #     return render(request, "ppaps/create.html", context)
    # else:
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     Review.objects.create(title=title, content=content)
    #     return redirect("/")
    if request.method == 'POST':
        ppaps_form = ReviewForm(request.POST)
        if ppaps_form.is_valid():
            ppaps_form.save()
            return redirect("/")
    else:
        ppaps_form = ReviewForm()
    context = {
        "ppaps_form" : ppaps_form
    }
    return render(request, 'ppaps/create.html', context)
    
    
def detail(request, pk):
    k = Review.objects.get(pk=pk)
    context = {
        "v" : k
    }
    return render(request, "ppaps/detail.html", context)

def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect("/")

def update(request, pk):
    # k = Review.objects.get(pk=pk)
    
    # if request.method == "POST":
    #     k.title = request.POST.get('title')
    #     k.content = request.POST.get('content')
    #     k.save()
    #     return redirect("/")
    # else:
    #     context = {
    #         "c" : k
    #     }
    # return render(request, 'ppaps/update.html', context)
    k = Review.objects.get(pk=pk)
    
    if request.method == "POST":
        ppaps_form = ReviewForm(request.POST, instance=k)
        if ppaps_form.is_valid():
            ppaps_form.save()
            return redirect("/", k.pk)
    else:
        ppaps_form = ReviewForm(instance=k)
    context = {
        "ppaps_form" : ppaps_form,
        "c" : k,
    }

    return render(request, 'ppaps/update.html', context)