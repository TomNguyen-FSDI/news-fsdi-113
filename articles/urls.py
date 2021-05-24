from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

urlpatterns = [
    path('', ArticleListView.as_view(),  name='article_list'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(),  name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(),  name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(),  name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name="article_new"),
    path('new/comment/', CommentCreateView.as_view(), name="create_comment"),
    path('<int:pk>/comment/edit/', CommentUpdateView.as_view(),  name='comment_edit'),
    path('<int:pk>/comment/delete/', CommentDeleteView.as_view(),  name='comment_delete'),
]