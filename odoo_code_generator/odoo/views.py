from django.urls import reverse_lazy
from django.views import generic
from .models import OdooReport


class OdooReportListView(generic.ListView):
    model = OdooReport


class OdooReportCreateView(generic.CreateView):
    model = OdooReport
    fields = ['model_name']


class OdooReportUpdateView(generic.UpdateView):
    model = OdooReport
    fields = ['model_name']


class OdooReportDetailView(generic.DetailView):
    model = OdooReport


class OdooReportDeleteView(generic.DeleteView):
    model = OdooReport
    success_url = reverse_lazy('odooreport-list')