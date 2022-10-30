from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from .models import Project
from .forms import ProjectForm
# Create your views here.

class ProjectListView(ListView):
    model = Project
    object_context_name = 'project_list'
    template_name = 'project/project_list.html'

class ProjectCreateFormView(FormView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def dispatch(self, request):
        if not request.user.is_authenticated:
            response = render(request, '404.html')
            response.status_code = 404
            return response
        else:
            return super().dispatch(request)

class ProjectUpdateView(UpdateView):
    fields = '__all__'
    model = Project
    template_name = 'project/project_update.html'

    def dispatch(self, request, pk):
        if not request.user.is_authenticated:
            response = render(request, '404.html')
            response.status_code = 404
            return response
        else:
            return super().dispatch(request)

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/project_delete.html'

    success_url = '/'