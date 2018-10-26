from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LostForm, FoundForm


def lost(request):
    if request.method == "POST":
        lost_form = LostForm(data=request.POST)
        if lost_form.is_valid():
            lost_item = lost_form.save(commit=False)
            lost_item.save()
    else:
        lost_form = LostForm()
    return render(request, 'lostandfound/lost.html', {'lost_form': lost_form})


def found(request):
    if request.method == "POST":
        found_form = FoundForm(data=request.POST)
        if found_form.is_valid():
            found_item = found_form.save(commit=False)
            found_item.save()
    else:
        found_form = FoundForm()
    return render(request, 'lostandfound/found.html', {'found_form': found_form})

