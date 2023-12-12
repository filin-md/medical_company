from django.urls import path

from main.views import AnalysisListView, DoctorListView, DoctorDetailView, AnalysisDetailView, OrderCreateView, contacts

app_name = 'main'

urlpatterns = [
    path('', AnalysisListView.as_view(), name='analysis_list'),
    path('doctors/', DoctorListView.as_view(), name='doctors_list'),
    path('doctor/<int:pk>', DoctorDetailView.as_view(), name='doctor_detail'),
    path('analysis/<int:pk>', AnalysisDetailView.as_view(), name='analysis_detail'),
    path('order/', OrderCreateView.as_view(), name='order'),
    path('contacts/', contacts, name='contacts'),

]