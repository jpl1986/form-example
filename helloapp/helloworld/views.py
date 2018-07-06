# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from .forms import NameForm

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        form = NameForm()
        return render(request, 'index.html', {'form':form})
        #return render(request, 'index.html', {'form': form})

class AboutPageView(TemplateView):
    template_name = "about.html"

class NamePageView(TemplateView):
    template_name = "yourname.html"

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            firstname = form.cleaned_data['firstname']
            surname = form.cleaned_data['surname']
            birthdate = form.cleaned_data['birthdate']
            # redirect to a new URL:
            #return HttpResponseRedirect('yourname.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        #your_name = form.cleaned_data['your_name']
    return render(request, 'yourname.html', {'firstname':firstname, 'surname':surname, 'birthdate':birthdate})
