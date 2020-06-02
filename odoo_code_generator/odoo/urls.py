from django.urls import path
from .views import OdooReportListView, OdooReportCreateView, OdooReportUpdateView, OdooReportDeleteView, OdooReportDetailView

app_name = 'odoo'
urlpatterns = [
    path('odooreports/', OdooReportListView.as_view(), name='odooreport-list'),
    path('odooreports/create/', OdooReportCreateView.as_view(), name='odooreport-form'),
    path('odooreports/<int:pk>/update', OdooReportUpdateView.as_view(), name='odooreport-update'),
    path('odooreports/<int:pk>/detail', OdooReportDetailView.as_view(), name='odooreport-detail'),
    path('odooreports/<int:pk>/delete', OdooReportDeleteView.as_view(), name='odooreport-delete'),
]