from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project, Suite, Case


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'tms/project/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['project_suites'] = Suite.objects.filter(project=self.kwargs.get('pk'))
        return context


class ProjectListView(ListView):
    model = Project
    template_name = 'tms/project/project_list.html'
    context_object_name = 'projects'


class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description']
    template_name_suffix = "/project_form"


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'description']
    template_name_suffix = "/project_form"


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = '/'


class SuiteDetailView(DetailView):
    model = Suite
    template_name = 'tms/suite_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SuiteDetailView, self).get_context_data(**kwargs)
        context['suite_cases'] = Case.objects.filter(suite=self.kwargs.get('pk'))
        return context


class SuiteCreateView(CreateView):
    model = Suite
    fields = ['name', 'description']
    template_name_suffix = "_form"


class SuiteUpdateView(UpdateView):
    model = Suite
    fields = ['name', 'description']
    template_name_suffix = "_form"


class SuiteDeleteView(DeleteView):
    model = Suite
    template_name = 'tms/suite_confirm_delete.html'
    success_url = '/'


class CaseDetailView(DetailView):
    model = Case
    template_name = 'tms/case/case_detail.html'
    context_object_name = 'case'


class CaseCreateView(CreateView):
    model = Case
    fields = ['suite', 'name', 'description', 'pre_requisites', 'test_steps',
              'case_status', 'automated']
    template_name_suffix = "/case_form"


class CaseUpdateView(UpdateView):
    model = Case
    fields = ['name', 'description']
    template_name_suffix = "/case_form"


class CaseDeleteView(DeleteView):
    model = Case
    success_url = '/'
