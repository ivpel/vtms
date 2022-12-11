from django.urls import path
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from . import views


app_name = 'tms'
urlpatterns = [
    # Homepage
    path('', views.homepage, name='homepage'),

    # User
    path('profile/', views.profile, name='profile'),
    path('login/', LoginView.as_view(authentication_form=LoginForm), name="login"),

    # Project
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('project/create', views.ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/detail', views.ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/update', views.ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete', views.ProjectDeleteView.as_view(), name='project_delete'),

    # Suite
    path('suite/create', views.SuiteCreateView.as_view(), name='suite_create'),
    path('suite/<int:pk>/detail', views.SuiteDetailView.as_view(), name='suite_detail'),
    path('suite/<int:pk>/update', views.SuiteUpdateView.as_view(), name='suite_update'),
    path('suite/<int:pk>/delete', views.SuiteDeleteView.as_view(), name='suite_delete'),

    # Case
    path('case/create', views.CaseCreateView.as_view(), name='case_create'),
    path('case/<int:pk>/', views.CaseDetailView.as_view(), name='case_detail'),
    path('case/<int:pk>/update', views.CaseUpdateView.as_view(), name='case_update'),
    path('case/<int:pk>/delete', views.CaseDeleteView.as_view(), name='case_delete'),
]
