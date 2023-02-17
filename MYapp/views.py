from django.shortcuts import render
from MYapp.models import Company
from django.views.generic import *
from django.urls import reverse_lazy
# Create your views here.
class CompanyListView(ListView):
    model = Company

class CompanyDetailView(DetailView):
    model = Company

class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'

class CompanyUpdateView(UpdateView):
    model = Company
    fields = '__all__'

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('companies')