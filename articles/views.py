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
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ('title', 'body',)

    def form_valid(self, form): # for LoginRequiredMixin
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ('title', 'body')

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
