from django.shortcuts import render

from .forms import ExampleForm


def index(request):
    form = ExampleForm()
    return render(request, 'app/index.html', {'form': form})
