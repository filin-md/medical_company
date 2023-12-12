from django.forms import DateTimeInput
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from main.models import Analysis, Doctor, Order


# Create your views here.


class AnalysisListView(ListView):
    model = Analysis


class AnalysisDetailView(DetailView):
    model = Analysis


class DoctorListView(ListView):
    model = Doctor


class DoctorDetailView(DetailView):
    model = Doctor


class OrderCreateView(CreateView):
    model = Order
    fields = 'doctor', 'consultation_date', 'client', 'phone'
    success_url = reverse_lazy('main:analysis_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['consultation_date'].widget = DateTimeInput(attrs={'type': 'datetime-local', 'step': 1800})
        return form



def contacts(request):
    return render(request, 'main/contacts.html')


