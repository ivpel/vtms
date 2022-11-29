from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Suite, Case


class SuiteDetailView(DetailView):
    model = Suite
    template_name = 'tms/suite_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SuiteDetailView, self).get_context_data(**kwargs)
        context['suite_cases'] = Case.objects.filter(suite=self.kwargs.get('pk'))
        return context


class SuiteListView(ListView):
    model = Suite
    template_name = 'tms/index.html'
    context_object_name = 'suites'


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
    template_name = 'tms/case_detail.html'
    context_object_name = 'case'
