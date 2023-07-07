from django.shortcuts import render, HttpResponseRedirect
from Handler.forms import ID_Form
from Practice2023.settings import BASE_DIR
import json

# Create your views here.
def index(request):
    result = {
        'id': '',
        'name': '',
        'description': '',
        'rating': '',
        'awesome': ''
    }
    form = ID_Form()
    if request.method == 'POST':
        id = int(request.POST.get('ID'))
        with open(BASE_DIR/'package.json') as f:
            films = json.load(f)
        for film in films:
            if film['id']== id:
                result = film


        context = {
            'form': form,
            'film': result
        }
        print(result)
        return render(request, 'Handler.html', context)
    context = {
        'form': form,
        'film': result
    }
    return render(request, 'Handler.html', context)