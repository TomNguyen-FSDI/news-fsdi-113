from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView
)
from django.views.generic.edit import (
    UpdateView,
    DeleteView,
    CreateView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.urls import reverse_lazy
from .models import Article, Comment
from .forms import CommentForm


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ('title', 'body', 'image')

    def form_valid(self, form): # for LoginRequiredMixin
        form.instance.author = self.request.user
        return super().form_valid(form)



class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  # Your part form
        return context




class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ('title', 'body', 'image')

    def test_func(self): # for UserPassesTestMixin
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "comment_new.html"
    fields = ('comment', 'star','author','article') 
    # print(dir(model))
    ## print(model.objects.values_list('article', flat=True))
    ## print(dir(model.objects))
    ## print(dir(model.objects.model))
    ## print(model.objects.model.pk)
    ## print(dir(model.author))
    ## print(dir(model.author.field))
    ## print(model.article.field)

    def form_valid(self, form): # for LoginRequiredMixin
        # print(self.request.article)
        # print(self.request.user)
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # def test_func(self): # for UserPassesTestMixin
    #     obj = self.get_object()
    #     return obj.author == self.request.user

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'comment_edit.html'
    fields = ('comment', 'star')

    def form_valid(self, form): # for LoginRequiredMixin
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    def test_func(self): # for UserPassesTestMixin
        obj = self.get_object()
        return obj.author == self.request.user

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user