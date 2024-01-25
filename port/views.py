from django.shortcuts import render

from django.views.generic import ListView, DetailView

from port.models import Port

# Create your views here.
    
class PortLV(ListView):
    model = Port

class PortDV(DetailView):
    model = Port