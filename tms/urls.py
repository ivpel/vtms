from django.urls import path

from . import views

urlpatterns = [
    # Suite
    path('', views.SuiteListView.as_view(), name='index'),
    path('suite/<int:pk>/detail', views.SuiteDetailView.as_view(), name='suite_detail'),
    path('suite/create', views.SuiteCreateView.as_view(), name='suite_create'),
    path('suite/<int:pk>/update', views.SuiteUpdateView.as_view(), name='suite_update'),
    path('suite/<int:pk>/delete', views.SuiteDeleteView.as_view(), name='suite_delete'),

    # Case
    path('case/<int:pk>/', views.CaseDetailView.as_view(), name='case_detail'),
]
app_name = 'tms'
