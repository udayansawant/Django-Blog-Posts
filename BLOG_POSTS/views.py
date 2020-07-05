from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib import messages
from django.urls import reverse_lazy
# from django.http import HttpResponse


#def index(request):
#    return render(request, 'BLOG_POSTS/POST_LIST.html')

class Index(ListView):
    model = Post
    template_name = 'BLOG_POSTS/index.html'

class PostList(DetailView):
    model = Post
    template_name = 'BLOG_POSTS/POST_LIST.html'

class PostForm(CreateView):
    model = Post
    template_name = 'BLOG_POSTS/POST_FORM.html'
    fields = '__all__'

class PostEdit(UpdateView):
    model = Post
    template_name = 'BLOG_POSTS/POST_EDIT.html'
    fields = ['title', 'body']


class PostDelete(DeleteView):
    model = Post
    template_name = 'BLOG_POSTS/POST_DELETE.html'
    success_url = reverse_lazy('index')

def new_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        body = request.POST['body']
        post_date = request.POST['post_date']
        photo_main = request.POST['photo_main']
        post = Post.objects.create(title=title, author=author, body=body, post_date=post_date, photo_main=photo_main)
        post.save()
        messages.success(request, 'Your Post published!')
        return redirect('index')

