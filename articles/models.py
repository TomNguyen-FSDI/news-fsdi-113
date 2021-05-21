from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user, get_user_model
from django.db import models
from django.urls import reverse



class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),       # the user that is creating the model
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # /article/<id>
        return reverse("article_detail", args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE,
        related_name="comments"
        )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )


    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('articles_list')