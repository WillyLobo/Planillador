from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from fallout.models import CharFallout
from fallout.forms import PlanillaFalloutForm

# Create your views here.
def falloutindex(request):
    template_name = "planilla-fallout.html"
    return render(request, template_name)

class PlanillaFalloutDetailView(UpdateView):
    model = CharFallout
    template_name = "planilla-fallout.html"
    form_class = PlanillaFalloutForm

class PlanillaFalloutCreateView(CreateView):
    model = CharFallout
    template_name = "planilla-fallout.html"
    form_class = PlanillaFalloutForm

