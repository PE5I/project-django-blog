from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import FormView
from .forms import PostForm

from .models import Post

class PostListView(ListView):
    model = Post 
    context_object_name = 'post_list'
    template_name = 'blog/blog_list.html'

class PostDetailView(DetailView):
    model = Post 
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'

class PostCreateFormView(FormView):
    template_name = 'blog/blog_create.html'
    form_class = PostForm
    success_url = '/blog/'

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

class PostUpdateView(UpdateView):
    fields = '__all__'
    model = Post
    template_name = 'blog/blog_update.html'

    def dispatch(self, request, slug):
        if not request.user.is_authenticated:
            response = render(request, '404.html')
            response.status_code = 404
            return response
        else:
            return super().dispatch(request)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/blog_delete.html'

    success_url = '/blog/'