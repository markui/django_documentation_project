from django.shortcuts import render
from model.forms import PersonForm
# Create your views here.


def show_model(request):
    form = PersonForm()
    context = {
        'form': form
    }
    return render(request, 'model.html', context)
