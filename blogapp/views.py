from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here
def LikeView(request, pk):
     # post = get_object_or_404(request, id=request.POST.get('post_id'))
     # post = get_object_or_404(Post, pk=pk)
     # post.likes.add(request.user)
     # return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

     post = get_object_or_404(Post, pk=pk)
     post.likes.add(request.user)
     return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


def logout_view(request):
    logout(request)
    return redirect('home')

class HomeView(ListView):
    model = Post
    template_name = 'blogapp/index.html'
    ordering = ['-post_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogapp/postdetail.html'
   
#     def get_context_data(self, *args, **kwargs):
#         context = {}
#         stuff = get_object_or_404(Post, id=self.kwargs['pk'])
#         total_likes = stuff.total_likes()
#         context["total_likes"] = total_likes
#         return contexts


class AddPostView(CreateView):
     model = Post
     form_class = PostForm
     template_name = 'blogapp/addpost.html'
     #fields = '__all__'

def CategoryView(request, cats):
     category_posts = Post.objects.filter(category = cats.replace('-', ' '))
     return render(request, 'blogapp/categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts': category_posts})

class AddCatView(CreateView):
     model = Category
     #form_class = PostForm
     template_name = 'blogapp/addcat.html'
     fields = '__all__'

class UpdatePostView(UpdateView):
     model = Post
     form_class = EditForm
     template_name = 'blogapp/addpost.html'
     #fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
     model = Post
     template_name = 'blogapp/deletepost.html'
     success_url = reverse_lazy('home')