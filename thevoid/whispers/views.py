from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Interpretation
from .forms import InterpretationForm

def index(request):

  if request.method == 'POST':

    form = InterpretationForm(request.POST)
    
    if form.is_valid():
        interp = form.cleaned_data['interpretation']
        p = Interpretation(text=interp)
        p.save()

        return HttpResponseRedirect('')
 
  else: 
    form = InterpretationForm()

  return render(request, 'interpretations.html', {'form': form})