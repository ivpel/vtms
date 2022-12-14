from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user
from .models import Project, Suite, Case


class LoginRequired(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


def homepage(request):
    return render(request, 'homepage.html')


@login_required(login_url='/login/')
def profile(request):
    user = get_user(request)
    return render(request, 'registration/profile.html', {'user': user})


class ProjectDetailView(LoginRequired, DetailView):
    model = Project
    template_name = 'tms/project/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['project_suites'] = Suite.objects.filter(project=self.kwargs.get('pk'))
        return context


class ProjectListView(LoginRequired, ListView):
    model = Project
    template_name = 'tms/project/project_list.html'
    context_object_name = 'projects'


class ProjectCreateView(LoginRequired, CreateView):
    model = Project
    fields = ['name', 'description']
    template_name_suffix = "/project_form"


class ProjectUpdateView(LoginRequired, UpdateView):
    model = Project
    fields = ['name', 'description']
    template_name_suffix = "/project_form"


class ProjectDeleteView(LoginRequired, DeleteView):
    model = Project
    success_url = '/'


class SuiteDetailView(LoginRequired, DetailView):
    model = Suite
    template_name = 'tms/suite/suite_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SuiteDetailView, self).get_context_data(**kwargs)
        context['suite_cases'] = Case.objects.filter(suite=self.kwargs.get('pk'))
        return context


class SuiteCreateView(LoginRequired, CreateView):
    model = Suite
    fields = ['name', 'description', 'project']
    template_name_suffix = "/suite_form"


class SuiteUpdateView(LoginRequired, UpdateView):
    model = Suite
    fields = ['name', 'description']
    template_name_suffix = "/suite_form"


class SuiteDeleteView(LoginRequired, DeleteView):
    model = Suite
    template_name = 'tms/suite/suite_confirm_delete.html'
    success_url = '/'


class CaseDetailView(LoginRequired, DetailView):
    model = Case
    template_name = 'tms/case/case_detail.html'
    context_object_name = 'case'


class CaseCreateView(LoginRequired, CreateView):
    model = Case
    fields = ['suite', 'name', 'description', 'pre_requisites', 'test_steps',
              'case_status', 'automated']
    template_name_suffix = "/case_form"


class CaseUpdateView(LoginRequired, UpdateView):
    model = Case
    fields = ['name', 'description']
    template_name_suffix = "/case_form"


class CaseDeleteView(LoginRequired, DeleteView):
    model = Case
    success_url = '/'
